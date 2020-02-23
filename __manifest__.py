{
    'name':'Excise Tracker',
    'description':'Track excise on movements of goods subject to excise',
    'author':'James Carr-Saunders',
    'depends':['stock'],
    'application':True,
    'installable': True,
    'data': [
#        'data/barcodes_data.xml',
#        'views/barcodes_view.xml',
        'security/ir.model.access.csv',
#        'views/barcodes_templates.xml',
    ],
}