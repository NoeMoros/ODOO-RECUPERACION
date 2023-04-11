# -*- coding: utf-8 -*-
{
    'name': "recu2",
    'summary': """recu2""",
    'description': """Odoo module to buy 2nd hand laptops:""",
    'author': "recu2",
    'website': "https://github.com/SalesianosZaragoza/recuperacion-odoo-jonfeddan.git",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',
    'application': True,
    'sequence': -100,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/chat.xml',
        'views/envio.xml',
        'views/marca.xml',
        'views/mensaje.xml',
        'views/portatil.xml',
        'views/post_venta.xml',
        'views/producto.xml',
        'views/usuario.xml',
        'views/venta.xml',
        'views/menus.xml',
    ],
}
