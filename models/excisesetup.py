from odoo import api, fields, models

class excise_category(models.Model):
    #https://www.gov.uk/government/publications/rates-and-allowance-excise-duty-alcohol-duty/alcohol-duty-rates-from-24-march-2014
    _name = 'excise_category'
    _description = 'Excise Category'


    category_code = fields.Char(
        'Code',
        default=None,
        index=True,
        readonly=False,
        required=True,
        translate=False)
    name = fields.Text('Description', index=True, required=True)
    tech_name = fields.Text('Technical Description')
    rate_per = fields.Selection([
        ('hectoabv','Rate per hectolitre per cent of alcohol in the beer'),
        ('hectoprod','Rate per hectolitre of product'),
        ('litrealco','Rate per litre of pure alcohol')
    ])
    add_cat = fields.Many2one('excise_category','Additional Category')