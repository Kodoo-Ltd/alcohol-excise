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
    rate = fields.Monetary(compute='_compute_current_rate', string='Current Rate', digits=0,
                    help='The rate of the currency to the currency of rate 1.')

    add_cat = fields.Many2one('excise.category','Additional Category')
    date = fields.Date(compute='_compute_date')
    rate_ids = fields.One2many('excise.category.rate', 'category_id', string='Rates')
    currency_id = fields.Many2one('res.currency', string="Currency")

    @api.depends('rate_ids.rate') 
    def _compute_current_rate(self):
        date = self._context.get('date') or fields.Date.today()
        excise_rates = self._get_rates(date)
        for cat in self:
            cat.rate = excise_rates.get(cat.id) or 0

    def _get_rates(self,  date):
        self.env['excise.category.rate'].flush(['rate', 'category_id', 'name'])
        query = """SELECT ec.id,
                    COALESCE((SELECT ecr.rate FROM excise_category_rate ecr
                        WHERE category_id = ec.id AND ecr.name <= %s
                        ORDER BY "name" DESC
                        LIMIT 1), 1.0) AS ecr
                    FROM excise_category ec
                WHERE ec.id IN %s"""
        self._cr.execute(query, (date,  tuple(self.ids)))
        category_rates = dict(self._cr.fetchall())
        return category_rates

    @api.depends('rate_ids.name')
    def _compute_date(self):
        for category in self:
            category.date = category.rate_ids[:1].name

    #@api.model
    #def _calc_excise(self,product,quantity):
    #    values={}
    #    values['excise_abv'] = product.excise_abv
    #    values['excise_move_volume'] =  quantity * product.excise_volume 
    #    values['excise_alcohol'] = values.get('excise_move_volume') * product.excise_abv
    #    values['excise_category'] = product.excise_category
    #    values['excise_category_rate'] = product.excise_category.rate
    #    #if product.excise_category.add_cat:

    #    return(values)




class excise_category_rate(models.Model):
    _name = 'excise.category.rate'
    _description = 'Excise Rate'

    name = fields.Date(string='Start Date', required=True, index=True,
                           default=lambda self: fields.Date.today())
    category_id = fields.Many2one('excise.category', string='Category', readonly=True)
    rate = fields.Monetary('Rate')

    currency_id = fields.Many2one('res.currency', string="Currency", compute='_compute_currency', readonly = True)

    @api.depends('category_id')
    def _compute_currency(self):
        for ecr in self:
            ecr.currency_id = ecr.category_id.currency_id
