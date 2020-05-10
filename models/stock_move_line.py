from odoo import fields, models, api

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"
    excise_move_ids = fields.One2many('excise.move', 'stock_move_line_id', string='Excise Moves')

    @api.model
    def create(self,values):    
        sml = super().create(values)
        if not sml.move_id._requires_excise_move():
            return sml
        emvalues = {
            'name' : sml.move_id.name,
            'stock_move_line_id' : sml.id,            
            'stock_move_id' : sml.move_id.id,
            #'company_id' : sml.company_id,
            'product_id' : sml.product_id.id,       
            #'move_qty' : sml.product_qty,
        }
        if sml.qty_done == 0:
            _qty = sml.product_qty
        else:
            _qty = sml.qty_done
        excise_result = self.env['excise.category']._calc_excise(sml.product_id,_qty)
        emvalues.update(excise_result)
        if 'excise_categories' in excise_result:
            del emvalues['excise_categories']
            for cat in excise_result['excise_categories']:
                emvalues.update(cat)
                self.env['excise.move'].sudo().create(emvalues)    
        else:
            self.env['excise.move'].sudo().create(emvalues)
        return sml

    @api.model
    def write(self,values):
        super().write(values)
        if len(self) == 0:
            return True
        if not self.move_id._requires_excise_move():
            return True                       
        if self.qty_done == 0:
            _qty = self.product_qty
        else:
            _qty = self.qty_done
        for em in self.excise_move_ids:
            if em.move_qty != _qty:                             
                excise_result = self.env['excise.category']._calc_excise(self.product_id,_qty)
                em.move_qty = _qty
                em.excise_move_volume = excise_result['excise_move_volume']
                em.excise_alcohol = excise_result['excise_alcohol']
                for cat in excise_result['excise_categories']:
                    if cat['excise_category'] == em.excise_category.id:
                        em.excise_amount_tax = cat['excise_amount_tax']
        return True

