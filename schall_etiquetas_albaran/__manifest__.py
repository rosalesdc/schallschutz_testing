# -*- coding: utf-8 -*-
{
    'name': "Etiquetas Albaran",

    'summary': """
    """,

    'description': """
        Imprimir etiquetas de Albarán
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'barcodes',
    ],

    # always loaded
    'data': [
        'views/etiquetas_albaran_view.xml'
    ],
    'installable':True,
    'auto_install':False,
}
