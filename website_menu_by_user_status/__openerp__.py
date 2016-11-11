# -*- coding: utf-8 -*-
# © 2011 ClearCorp
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Website Menu By User Display',
    'summary': 'Allow to manage the display of website.menus',
    'version': '9.0.1.0',
    'category': 'Website',
    'website': 'http://clearcorp.cr',
    'author': 'ClearCorp',
    'license': 'AGPL-3',
    'sequence': 10,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': [
        'website'
    ],
    'data': [
        'views/website_templates.xml',
        'views/website_views.xml',
    ],
}