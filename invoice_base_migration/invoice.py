# -*- coding: utf-8 -*-
###############################################################################
#
#   Module for OpenERP
#   Copyright (C) 2014 Akretion (http://www.akretion.com).
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


class AccountInvoice(orm.Model):
    _inherit = 'account.invoice'

    def _get_invoice_number(self, cr, uid, ids, field_name, args, context=None):
        result = {}
        for invoice in self.browse(cr, uid, ids, context=context):
            if invoice.migrated:
                result[invoice.id] = invoice.internal_number
            else:
                result[invoice.id] = invoice.move_id.name
        return result

    _columns = {
        'migrated': fields.boolean('Migrated Invoice'),
        'number': fields.function(
            _get_invoice_number,
            string='Number',
            type='char',
            store=True,
            ),
    }

    _defaults = {
        'migrated': False,
    }
