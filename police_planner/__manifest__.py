# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
{
    'name': "Police Planificator",
    'version': '11.0.1.0.0',
    'author': "AbAKUS it-solutions SARL",
    'description': """
Police Planificator
    """,
    'license': 'AGPL-3',
    'website': "http://www.abakusitsolutions.eu",
    'depends': [
        'hr',
    ],
    'category': 'Planning',
    'data': [
        'views/menuitems.xml',

        'views/hr_employee.xml',
        'views/police_house.xml',
        'views/police_intervention_type.xml',
        'views/police_plan.xml',
        'views/police_zone.xml',
    ],
    'installable': True,
    'application': True,
}
