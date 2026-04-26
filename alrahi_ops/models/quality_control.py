from odoo import models, fields, api
from odoo.exceptions import UserError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # Checking the Roast_quality
    x_roast_quality = fields.Selection([
        ('pending', 'Pending'),
        ('passed', 'Passed'),
        ('failed', 'Failed')
    ], string="Roast Quality", default='pending', tracking=True)

    # Validation for Roast_Quality
    def button_validate(self):
        """ Overriding the Validate button to enforce Quality Checks """
        for record in self:
            # If the transfer is coming from the Roastery Internal quality check
            if record.picking_type_code == 'internal' and record.x_roast_quality == 'pending':
                raise UserError("Action Blocked: You must perform a Quality Check (Pass/Fail) before validating this transfer.")
            
            if record.x_roast_quality == 'failed':
                raise UserError("Action Blocked: This batch has FAILED quality control and cannot be moved to retail.")
        
        return super(StockPicking, self).button_validate()
