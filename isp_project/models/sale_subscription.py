from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleSubscription(models.Model):

    _inherit = ["sale.subscription"]

    customer_conf_id = fields.Many2one("isp.customer.configuration", string="Customer Configuration")

    def action_view_customer_confi(self):
        return {
            "type": "ir.actions.act_window",
            "res_model": "isp.customer.configuration",
            "domain": [("subscription_id", "=", self.id)],
            "name": self.name,
            "view_mode": "tree,form",
        }
