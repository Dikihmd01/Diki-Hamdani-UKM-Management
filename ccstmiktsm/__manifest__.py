# -*- coding: utf-8 -*-
{
    'name': "ccstmiktsm",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/member_views.xml',
        'views/sequence.xml',
        'views/event_type_views.xml',
        'views/event_views.xml',
        'views/incoming_letter_views.xml',
        'views/outcoming_letter_views.xml',
        'views/balance_views.xml',
        'views/income_views.xml',
        'views/outcome_views.xml',
        'report/report.xml',
        'report/export_incoming_letter_to_pdf.xml',
        'report/export_outcoming_letter_to_pdf.xml',
        'report/export_incoming_balance_to_pdf.xml',
        'report/export_outcoming_balance_to_pdf.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
