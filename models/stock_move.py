from odoo import fields, models, api
from odoo.exceptions import UserError

class StockMove(models.Model):
    _inherit = "stock.move"
    
    def _requires_excise_move(self):
        self.ensure_one()
        if not self.product_id.excise_active:
            return False
        if not self.location_id.excise_unpaid and self.location_dest_id.excise_unpaid:
            if self.location_id.usage == 'inventory':  #allow stock adjustments
                return True
            raise UserError("You cannot move excisable product from duty paid to duty unpaid")
        if self.location_id.excise_warehouse_no != self.location_dest_id.excise_warehouse_no:
            return True
        if self.location_id.excise_unpaid and not self.location_dest_id.excise_unpaid:
           return True
        return False
        