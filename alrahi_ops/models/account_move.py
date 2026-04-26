from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    # 1. Text Field: Customer TRN
    x_customer_trn = fields.Char(string="Customer TRN", help="Tax Registration Number")

    # 2. Selection Panel: Delivery Method
    x_delivery_type = fields.Selection([
        ('pickup', 'Self Pickup'),
        ('van', 'Alrahi Delivery Van'),
        ('courier', 'Third-Party Courier')
    ], string="Delivery Method", default='van')

    # 3. Date Field: Roasting Date
    x_roast_date = fields.Date(string="Roast Date")

    # 4. Integer Field: Batch Number
    x_batch_no = fields.Integer(string="Batch Reference")

    # 5. Boolean Field: Quality Certified
    x_quality_certified = fields.Boolean(string="Quality Certified", default=False)

    # 6. Many2one Field: Assigned Driver (Relational)
    x_driver_id = fields.Many2one('res.users', string="Assigned Driver")
