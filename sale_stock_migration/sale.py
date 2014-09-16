# -*- coding: utf-8 -*-
#############################################################
#
#  see licence in __openerp__.py
#  Copyright (C) 2014 Akretion (http://www.akretion.com).
#  @author David BEAL <david.beal@akretion.com>
#
#############################################################

from openerp.osv import orm, fields


class SaleOrder(orm.Model):
    _inherit = 'sale.order'

    _columns = {
        #'create_date': fields.datetime(
        #    'Create date'),
        'no_picking': fields.boolean('No Picking'),
    }

    def _create_pickings_and_procurements(self, cr, uid, order, order_lines,
                                          picking_id=False, context=None):
        #import pdb;pdb.set_trace()
        #if not order.company_id.start_picking_create \
        #        or order.create_date > order.company_id.start_picking_create:
        if not order.no_picking:
            super(SaleOrder, self)._create_pickings_and_procurements(
                cr, uid, order, order_lines, picking_id=picking_id, context=context)
        return True


#class ResCompany(orm.Model):
#    _inherit = 'res.company'
#
#    _columns = {
#        'start_picking_create': fields.datetime(
#            'Picking creation',
#            help="Before this time, sales order will not create stock pickings."
#                 " No view to modify this date, changes are directly "
#                 "done by admin user in database."),
#    }
