{
    'name':'Excise - Alcohol',
    'description':'Track excise on movements of alcoholic beverages subject to excise',
    'author':'James Carr-Saunders',
    'depends':['base','product','stock'],
    'application':True,
    'installable': True,
    'data': [
        'views/excise_category_views.xml',
        'views/product_template_excise.xml',
        'views/excise_menu.xml',
        #'views/stock_move_line.xml',
        'views/stock_warehouse_excise.xml',
        'security/ir.model.access.csv',
        'data/excise_category_data.xml',
        'data/excise_category_rate_data.xml',

    ],
}