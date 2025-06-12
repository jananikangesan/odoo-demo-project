{
    'name': 'My Custom Module',
    'version': '1.0',
    'summary': 'A simple custom module for Odoo 17',
    'description': 'This module demonstrates how to create a module in Odoo 17',
    'author': 'Your Name',
    'license': 'LGPL-3',
    'category': 'Tools',
    'depends': ['base','contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_record_view.xml',
        'views/student_profile_views.xml',
    ],
    'installable': True,
    'application': True,
}
