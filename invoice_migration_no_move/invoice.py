# -*- coding: utf-8 -*-
###############################################################################
#
#   Module for OpenERP
#   Copyright (C) 2013 Akretion (http://www.akretion.com).
#   @author Sébastien BEAU <sebastien.beau@akretion.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp.osv import fields, orm
import logging

_logger = logging.getLogger(__name__)


class AccountInvoice(orm.Model):
    _inherit = 'account.invoice'

    def _get_invoice_period_id(self, cr, uid, inv, context=None):
        period_obj = self.pool['account.period']
        if context is None:
            context = {}
        ctx = context.copy()
        period_id = inv.period_id and inv.period_id.id or False
        ctx.update(
            company_id=inv.company_id.id,
            account_period_prefer_normal=True,
            )
        if not period_id:
            period_ids = period_obj.\
                find(cr, uid, inv.date_invoice, context=ctx)
            period_id = period_ids and period_ids[0] or False
        return period_id

    def action_move_create(self, cr, uid, ids, context=None):
        period_obj = self.pool['account.period']
        no_move_period_ids = period_obj.search(cr, uid, [
            ['fiscalyear_id.no_move_line', '=', True]
            ], context=context)
        for inv in self.browse(cr, uid, ids, context=context):
            period_id = self._get_invoice_period_id(
                cr, uid, inv, context=context)
            if period_id in no_move_period_ids:
                _logger.info(
                    "From module invoice_migration_no_move : "
                    "Skip the move creation as the period is in "
                    "a fiscalyear without move")
                inv.write({'period_id': period_id, 'migrated': True})
            else:
                super(AccountInvoice, self).\
                    action_move_create(cr, uid, ids, context=context)
        return True

    def action_number(self, cr, uid, ids, context=None):
        #Invoice without move (mean migrated invoice) do not
        #need to run the action_number
        invoice_ids = self.search(cr, uid, [
            ['move_id', '!=', False],
            ['id', 'in', ids],
            ], context=context)
        return super(AccountInvoice, self).\
            action_number(cr, uid, invoice_ids, context=context)

    def test_paid(self, cr, uid, ids, *args):
        invoice = self.browse(cr, uid, ids[0])
        if invoice.state == 'open' and not invoice.move_id:
            return True
        return super(AccountInvoice, self).test_paid(cr, uid, ids, *args)

    #Migration Helper call it with webservice or what you want
    def delete_invoice_move(self, cr, uid, ids, context=None):
        move_obj = self.pool['account.move']
        if not ids:
            period_obj = self.pool['account.period']
            no_move_period_ids = period_obj.search(cr, uid, [
                ['fiscalyear_id.no_move_line', '=', True]
                ], context=context)
            ids = self.search(cr, uid, [
                ['period_id', 'in', no_move_period_ids],
                ['move_id', '!=', None],
                ], context=context)
       	_logger.info('Migrate %s invoice' %len(ids))
        while ids:
            process_ids = ids[:100]
            ids = ids[100:]
       	    _logger.info('Start migrating 100 invoices, %s invoice remaining' %len(ids))
            read_invoices = self.read(cr, uid, process_ids, context=context)
            move_ids = [inv['move_id'][0] for inv in read_invoices if inv['move_id']]
            self.write(cr, uid, process_ids, {'move_id': None, 'migrated': True}, context=context)
            posted_move_ids = move_obj.search(cr, uid, [
                ['id', 'in', move_ids],
                ['state', '!=', 'draft'],
                ], context=context)
            move_obj.button_cancel(cr, uid, posted_move_ids, context=context)
            move_obj.unlink(cr, uid, move_ids, context=context)
            cr.commit()
        return True
