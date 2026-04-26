from odoo import models, fields, api
from odoo.exceptions import UserError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # L2 Feature: Selection field with tracking
    x_roast_quality = fields.Selection([
        ('pending', 'Pending'),
        ('passed', 'Passed'),
        ('failed', 'Failed')
    ], string="Roast Quality", default='pending', tracking=True)

    # L3 Feature: Automated Validation Logic
    def button_validate(self):
        """ Overriding the Validate button to enforce Quality Checks """
        for record in self:
            # If the transfer is coming from the Roastery (Internal)
            if record.picking_type_code == 'internal' and record.x_roast_quality == 'pending':
                raise UserError("Action Blocked: You must perform a Quality Check (Pass/Fail) before validating this transfer.")
            
            if record.x_roast_quality == 'failed':
                raise UserError("Action Blocked: This batch has FAILED quality control and cannot be moved to retail.")
        
        return super(StockPicking, self).button_validate()
