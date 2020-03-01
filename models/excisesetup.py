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
    #rate_ids = fields.One2many('excise.category.rate', 'category_id', string='Rates')
    rate = fields.Float(compute='_compute_current_rate', string='Current Rate', digits=0,
                    help='The rate of the currency to the currency of rate 1.')

    add_cat = fields.Many2one('excise_category','Additional Category')

    #@api.depends(self) //date?
    def _compute_current_rate(self):
        #date = self._context.get('date') or fields.Date.today()
        #currency_rates = self._get_rates(company, date)
        for cat in self:
        #    cat.rate = currency_rates.get(currency.id) or 0
            cat.rate = 1


class excise_category_rate(models.Model):
    _name = 'excise.category.rate'
    _description = 'Excise Rate'

    name = fields.Date(string='Start Date', required=True, index=True,
                           default=lambda self: fields.Date.today())
    category_id = fields.Many2one('excise.category', string='Category', readonly=True)
    rate = fields.Float('Rate')
