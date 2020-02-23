from odoo import api, fields, models

class excise_category(models.Model):
    #https://www.gov.uk/government/publications/rates-and-allowance-excise-duty-alcohol-duty/alcohol-duty-rates-from-24-march-2014
    _name = 'excise.category'
    _description = 'Excise Category'

    name = fields.Text('Description', index=True, required=True)
    tech_name = fields.Text('Technical Description')
    rate_per = fields.Selection([
        ('hectoabv','Rate per hectolitre per cent of alcohol in the beer'),
        ('hectoprod','Rate per hectolitre of product'),   
        ('litrealco','Rate per litre of pure alcohol')
    ])
    add_cat = fields.Many2one('excise_category','Additional Category')