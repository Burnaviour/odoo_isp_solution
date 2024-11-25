from odoo import models, fields, api, _


class ISPCustomerConfiguration(models.Model):
    _name = "isp.customer.configuration"
    _description = "ISP Customer Network Configuration"

    name = fields.Char(
        string="Customer Reference", required=True, copy=False, readonly=True, index=True, default=lambda self: _("New")
    )
    subscription_id = fields.Many2one("sale.subscription", string="Subscription", required=True)
    subscription_state = fields.Char(related="subscription_id.stage_id.name", string="Subscription State", store=True)
    customer_id = fields.Many2one("res.partner", string="Customer", related="subscription_id.partner_id", store=True)
    state = fields.Selection(
        [("draft", "Draft"), ("active", "Active"), ("suspended", "Suspended"), ("cancelled", "Cancelled")],
        string="Status",
        default="draft",
        tracking=True,
    )
    # ip_address = fields.Char(
    #     string="IP Address",
    # )
    active = fields.Boolean(string="Active", default=True)
    dns_line_ids = fields.One2many("network.conf.lines", "customer_conf_id", string="DNS Lines")
    # mac_address = fields.Char(
    #     string="MAC Address",
    # )
    # vlan_ids = fields.Many2many("isp.vlans", string="VLANs")
    ip_method = fields.Selection([("dhcp", "DHCP"), ("static", "STATIC")], tracking=True)
    ip_protocol = fields.Selection([("ipv4", "IPV4"), ("ipv6", "IPV6")], tracking=True)

    def set_to_draft(self):
        self.state = "draft"

    def set_to_active(self):
        self.state = "active"

    def set_to_suspended(self):
        self.state = "suspended"

    def set_to_cancelled(self):
        self.state = "cancelled"

    @api.model_create_multi
    def create(self, vals_list):
        for rec in vals_list:
            if rec.get("name", _("New")) == _("New"):
                rec["name"] = self.env["ir.sequence"].next_by_code("isp.customer") or _("New")
        return super().create(vals_list)

    def _compute_display_name(self):
        for rec in self:
            if rec.name and rec.customer_id:

                rec.display_name = rec.name + " - " + rec.customer_id.name
            else:
                rec.display_name = _("New")
