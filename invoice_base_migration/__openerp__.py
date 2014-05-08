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

{'name': 'Invoice Base Migration',
 'version': '0.0.1',
 'author': 'Akretion',
 'website': 'www.akretion.com',
 'license': 'AGPL-3',
 'category': 'Generic Modules/Migration',
 'description': """This Module will simply take the number of the invoice
 from the field internal_number instead of using the name of the move related.
 This allow to have invoice without move (for migration purpose) and to keep
 visible the invoice number.

 This module will no impact the move creation, and wil stay installed
 if you want to import invoice without move use the module
 'invoice_migration_no_move'. But be careful the module
 'invoice_migration_no_move' must be uninstalled before going in
 production. It's only a temporary module that will help you during
 the migration process.
 """,
 'depends': [
     'account',
 ],
 'data': [
 ],
 'installable': True,
 'application': True,
}
