# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Vlanids(models.Model):
    _name = "isp.vlans"
    _description = "VLAN IDs"
    _rec_name = "vlans"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    vlans = fields.Char(string="VLAN", tracking=True)
    assigned = fields.Boolean(string="Assigned", default=False)
    assigned_to = fields.Many2one("res.partner", string="Assigned to")
    crm_id = fields.Many2one(comodel_name="crm.lead", string="CRM ID")
    order_id = fields.Many2one(comodel_name="sale.order", string="Order ID")

    # ---> Keeping track of the vlans.
    lead_ids = fields.Many2many("crm.lead", string="Lead IDs")
    partner_ids = fields.Many2many("res.partner", string="Partner IDs")
    order_ids = fields.Many2many("sale.order", string="Order IDs")

    lead_count = fields.Integer(string="Lead Count", compute="_compute_lead_count", store=True)
    partner_count = fields.Integer(string="Partner Count", compute="_compute_partner_count", store=True)
    order_count = fields.Integer(string="Order Count", compute="_compute_order_count", store=True)

    # sql_constraints = [("vlan_unique", "unique(vlans)", "Vlan must be unique!")]

    @api.constrains("vlans")
    def _check_vlan(self):
        for record in self:
            vlans = self.env["isp.vlans"].sudo().search([("id", "!=", record.id)]).mapped("vlans")
            if record.vlans in vlans:
                raise ValidationError("Vlan already exists!")

    @api.depends("lead_ids")
    def _compute_lead_count(self):
        for record in self:
            record.lead_count = len(record.lead_ids)

    @api.depends("partner_ids")
    def _compute_partner_count(self):
        for record in self:
            record.partner_count = len(record.partner_ids)

    @api.depends("order_ids")
    def _compute_order_count(self):
        for record in self:
            record.order_count = len(record.order_ids)

    def open_leads(self):
        return {
            "name": _("Leads"),
            "domain": [("id", "in", self.lead_ids.ids)],
            "view_mode": "tree,form",
            "res_model": "crm.lead",
            "type": "ir.actions.act_window",
            "context": "{'create': False , 'open': False, 'edit': False}",
        }

    def open_order_ids(self):
        return {
            "name": _("Orders"),
            "domain": [("id", "in", self.order_ids.ids)],
            "view_mode": "tree,form",
            "res_model": "sale.order",
            "type": "ir.actions.act_window",
            "context": "{'create': False , 'open': False, 'edit': False}",
        }

    def open_partner_ids(self):
        return {
            "name": _("Partners"),
            "domain": [("id", "in", self.partner_ids.ids)],
            "view_mode": "tree,form",
            "res_model": "res.partner",
            "type": "ir.actions.act_window",
            "context": "{'create': False , 'open': False, 'edit': False}",
        }
