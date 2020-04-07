from odoo import api, fields, models

class excise_line(models.Model):
    _name = 'excise.move'
    _description = 'Excise Line'

    name = fields.Text('Description', index=True, required=True)
    stock_move_id = fields.Many2one(
        'stock.move', 'Stock Move',
        check_company=True,index=True)
    stock_move_line_id = fields.Many2one(
        'stock.move.line', 'Stock Move Line',
        check_company=True,index=True)
    company_id = fields.Many2one('res.company', string='Company', readonly=True, index=True)
    currency_id = fields.Many2one('res.currency', string="Currency",readonly=True)
    product_id = fields.Many2one('product.product', 'Product', check_company=True, domain="[('type', '!=', 'service'), '|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    move_qty = fields.Float('Movement Quantity', default=0.0, digits='Product Unit of Measure', copy=False)

    excise_abv = fields.Float('ABV',help='Average By Volume (% Alcohol)',readonly=True)
    excise_move_volume = fields.Float('Excisable Volume (L)', help='Volume being moved for the basis of the Excise calculation')
    excise_alcohol = fields.Float('Volume of alcohol (L)',readonly=True)
    excise_category = fields.Many2one('excise.category','Excise Category',readonly=True)
    excise_rate = fields.Monetary('Rate',readonly=True)
    excise_amount_tax = fields.Monetary(string='Excise Amount', readonly=True)
    #excise_category_add = fields.Many2one('excise.category','Additional Excise Category',readonly=True)
    #excise_amount_tax_add = fields.Monetary(string='Additional Excise Amount', readonly=True)
    #excise_payable = fields.Monetary(string='Total Excise Amount.',help='Total excise payable after releifs (e.g. samll brewers allowance)',readonly=True)

