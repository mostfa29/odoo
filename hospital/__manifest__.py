# -*- coding: utf-8 -*-
{
    'name': 'hospital manegment',
    'version': '1.2',
    'summary': 'hospital manegment',
    'sequence': -100,
    'description': """hospital manegment""",
    'category': 'managment',
    'author': 'Mostfa',
    'maintainer': 'Mostfa',
    'website': '',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'mail',
                'hr',


    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',

        'wizard/create_appointment_view.xml',
        'wizard/search_appointment_view.xml',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/appointment_view.xml',
        'views/kids_view.xml',
        'views/patient_gender_view.xml',
        'views/sale.xml',
        'report/patient_details_template.xml',
        'report/patient_card.xml',
        'report/report.xml'
    ],
    'demo': [],
    'qweb': [],
    'images': [''],
    'installable': True,
    'application': True,
    'auto_install': False,
}
