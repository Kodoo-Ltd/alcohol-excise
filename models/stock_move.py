from odoo import fields, models, api

class StockMove(models.Model):
    _inherit = "stock.move"
    #These are static fields as they form the basis of tax records and therefore should not be subject to change. 
    excise_abv = fields.Float('ABV',help='Average By Volume (% Alcohol)',readonly=True)
    excise_move_volume = fields.Float('Excisable Volume (L)', help='Volume being moved for the basis of the Excise calculation')
    excise_alcohol = fields.Float('Volume of alcohol (L)',readonly=True)
    excise_category = fields.Many2one('excise.category','Excise Category',readonly=True)
    #excise_amount_tax = fields.Monetary(string='Excise Amount', readonly=True)
    excise_category_add = fields.Many2one('excise.category','Additional Excise Category',readonly=True)
    #excise_amount_tax_add = fields.Monetary(string='Additional Excise Amount', readonly=True)
    #excise_payable = fields.Monetary(string='Total Excise Amount.',help='Total excise payable after releifs (e.g. samll brewers allowance)',readonly=True)

    excise_test = fields.Char('test field')


    @api.model
    def create(self,values):    
        if 'product_id' in values:
            product = self.env['product.product'].browse(values.get('product_id'))
            
            if product.excise_active:                                
                values['excise_abv'] = product.excise_abv
                values['excise_move_volume'] =  values.get('product_uom_qty') * product.excise_volume 
                values['excise_alcohol'] = values.get('excise_move_volume') * values.get('excise_abv')
                values['excise_category'] = product.excise_category.id

                values['excise_test'] = "Rate is %s" % product.excise_category.rate

                
        return super().create(values)
    
