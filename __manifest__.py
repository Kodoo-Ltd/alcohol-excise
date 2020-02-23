{
    'name':'Excise Tracker',
    'description':'Track excise on movements of goods subject to excise',
    'author':'James Carr-Saunders',
    'depends':['stock'],
    'application':True,
    'installable': True,
    'data': [
        'views/excise_category_tree.xml',
        'views/excise_menu.xml',
        'security/ir.model.access.csv',
#        'views/barcodes_templates.xml',
    ],
}