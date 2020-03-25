from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    excise_warehouse_no = fields.Char('Warehouse No.', help='number issued by tax authority to suspend excise liablity')
