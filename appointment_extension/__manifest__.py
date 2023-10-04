# -*- coding: utf-8 -*-
{
    'name': "appointment_extension",

    'summary': """
       Appointment Calender Event Extension""",

    'description': """
        Appointment Calender Event Extension
    """,
    'author': "Jamsheena kc",
    'website': "http://www.sgt.com",
    'category': 'appointment',
    'version': '0.1',
    'depends': ['appointment','website_appointment','account'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move.xml',
        'views/appointment_calender.xml',
        'views/appointment_portal_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    "images": ['static/description/icon.png'],
}