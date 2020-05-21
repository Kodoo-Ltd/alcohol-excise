from odoo import api, fields, models

class excise_move(models.Model):
    _name = 'excise.move'
    _description = 'Excise Line'

    name = fields.Text('Description', index=True, required=True)
    stock_move_id = fields.Many2one(
        'stock.move', 'Stock Move',
        check_company=True,index=True)
    stock_move_line_id = fields.Many2one(
        'stock.move.line', 'Stock Move Line',
        check_company=True,index=True)
    date = fields.Datetime(
        'Date', default=fields.Datetime.now, index=True, required=True,
        readonly= True,compute='_compute_move',store=True)
    company_id = fields.Many2one('res.company', string='Company', readonly=True, index=True)
    currency_id = fields.Many2one('res.currency', string="Currency",readonly=True)
    product_id = fields.Many2one('product.product', 'Product', check_company=True, domain="[('type', '!=', 'service'), '|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    move_qty = fields.Float('Movement Quantity', default=0.0, digits='Product Unit of Measure', copy=False)
    move_state = fields.Selection([
        ('draft', 'New'), ('cancel', 'Cancelled'),
        ('waiting', 'Waiting Another Move'),
        ('confirmed', 'Waiting Availability'),
        ('partially_available', 'Partially Available'),
        ('assigned', 'Available'),
        ('done', 'Done')], string='Status',
        copy=False, default='draft', index=True, readonly=True,
        related='stock_move_id.state',store=True)   
    move_reference = fields.Char(related='stock_move_id.reference', string="Reference", store=True)
    move_location_id = fields.Many2one('stock.location', 'Source Location',
                related='stock_move_id.location_id', readonly=True)
    move_location_dest_id = fields.Many2one('stock.location', 'Destination Location',
                related='stock_move_id.location_dest_id', readonly=True)
    move_partner_id = fields.Many2one('res.partner', 'Destination Address ',
                related='stock_move_id.partner_id', readonly=True)

    excise_abv = fields.Float('ABV',help='Average By Volume (% Alcohol)',readonly=True)
    excise_move_volume = fields.Float('Excisable Volume (L)', help='Volume being moved for the basis of the Excise calculation')
    excise_alcohol = fields.Float('Volume of alcohol (L)',readonly=True)
    excise_category = fields.Many2one('excise.category','Excise Category',readonly=True)
    excise_rate = fields.Monetary('Rate',readonly=True)
    excise_amount_tax = fields.Monetary(string='Excise Amount', readonly=True)
    excise_payable = fields.Monetary(string='Total Excise Amount.',help='Total excise payable after releifs (e.g. samll brewers allowance)',readonly=True)


    #def _compute_move(self):
    #    for em in self:
    #        em.move_state = em.stock_move_id.state
    #        em.move_reference = em.stock_move_id.reference
    #        em.date = em.stock_move_id.date
    #        em.move_location_id = em.stock_move_id.location_id
    #        em.move_location_dest_id = em.stock_move_id.location_dest_id
    #        em.move_partner_id = em.stock_move_id.partner_id