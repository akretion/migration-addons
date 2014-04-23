# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: David BEAL
#    Copyright 2014 Akretion
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Sale Stock Migration',
    'version': '0.2',
    'author': 'Akretion',
    'maintainer': 'Akretion',
    'category': 'tool',
    'depends': [
        'sale_stock',
    ],
    'description': """
Sale Stock Migration
==========================

Description
--------------
Base module for importing sales order historic without stock pickings.


Uninstall
------------
You may uninstall this module without any damage


Contributors
------------
* David BEAL <david.beal@akretion.com>
* Sébastien BEAU <sebastien.beau@akretion.com>

----

    """,
    'website': 'http://www.akretion.com/',
    'data': [
        #'stock_view.xml',
    ],
    'tests': [],
    'installable': True,
    'license': 'AGPL-3',
    'auto_install': False,
    'application': False,
}
