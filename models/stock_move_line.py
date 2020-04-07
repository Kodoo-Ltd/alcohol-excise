from odoo import fields, models, api

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"


    @api.model
    def create(self,values):    
        sml = super().create(values)
        emvalues = {
            'name' : sml.reference,
            'stock_move_line_id' : sml.id,            
            'stock_move_id' : sml.move_id.id,
            #'company_id' : sml.company_id,
            'product_id' : sml.product_id.id,       
            #'move_qty' : sml.product_qty,
        }
        excise_result = self.env['excise.category']._calc_excise(sml.product_id,sml.product_qty)
        emvalues.update(excise_result)
        if 'excise_categories' in excise_result:
            del emvalues['excise_categories']
            for cat in excise_result['excise_categories']:
                emvalues.update(cat)
                self.env['excise.move'].sudo().create(emvalues)    
        else:
            self.env['excise.move'].sudo().create(emvalues)
        return sml
