from odoo import fields, models


class Warehouse(models.Model):
    _inherit = 'stock.warehouse'

    excise_warehouse_no = fields.Char('Warehouse No.', help='number issued by tax authority to suspend excise liablity')
