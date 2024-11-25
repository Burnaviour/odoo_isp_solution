from odoo import models, fields, api


class ISPCustomerConfiguration(models.Model):
    _name = "isp.customer.configuration"
    _description = "ISP Customer Network Configuration"

    subscription_id = fields.Many2one("sale.subscription", string="Subscription", required=True)
    subscription_state = fields.Char(related="subscription_id.stage_id.name", string="Subscription State", store=True)
    customer_id = fields.Many2one("res.partner", string="Customer", related="subscription_id.partner_id", store=True)
    state = fields.Selection(
        [("draft", "Draft"), ("active", "Active"), ("suspended", "Suspended"), ("cancelled", "Cancelled")],
        string="Status",
        default="draft",
        tracking=True,
    )
    ip_address = fields.Char(
        string="IP Address",
    )
    active = fields.Boolean(string="Active", default=True)
    mac_address = fields.Char(
        string="MAC Address",
    )
    vlan_ids = fields.Many2many("isp.vlans", string="VLANs")

    def set_to_draft(self):
        self.state = "draft"

    def set_to_active(self):
        self.state = "active"

    def set_to_suspended(self):
        self.state = "suspended"

    def set_to_cancelled(self):
        self.state = "cancelled"
