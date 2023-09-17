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
    'depends': ['appointment','website_appointment','invoice'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move.xml',
        'views/appointment_calender.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}