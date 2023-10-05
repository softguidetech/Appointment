# -*- coding: utf-8 -*-
{
    'name': "appointment Extension",
    'author': "SGT",
    'version': '16.0.1.4',
    'price': 55.00,
    'currency': "EUR",
    
    'summary': """
       Appointment Calender Event Extension""",

    'description': """
        Appointment Calender Event Extension
    """,
    'website': "http://www.softguidetech.com",
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
    "images": ['static/description/icon.gif'],
}
