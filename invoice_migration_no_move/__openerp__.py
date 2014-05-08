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

{'name': 'Invoice Migration',
 'version': '0.0.1',
 'author': 'Akretion',
 'website': 'www.akretion.com',
 'license': 'AGPL-3',
 'category': 'Generic Modules',
 'description': """
 Becareful, this module will impact the move creation !
 If the option 'no_move_line' have been set on the fiscalyear, the invoice
 generated for this fiscalyear will not generate account_move.
 After the Migration process this module MUST BE uninstalled !!
 Indeed as in production you never never never want this process,
 so you have to uninstall it to avoid a potential trouble with other module
 """,
 'depends': [
     'invoice_base_migration',
 ],
 'update_xml': [
     'account_view.xml',
 ],
 'installable': True,
 'application': True,
}




