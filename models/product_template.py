fromo odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    excise_active = fields.boolean('Track Excise',default=False)