# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class NetworkConfLines(models.Model):
    _name = 'network.conf.lines'
    _description = 'Network Conf Lines'

    customer_conf_id = fields.Many2one("isp.customer.configuration", string="Customer Configuration")
    ipaddress = fields.Char(string="IP Address")
    pre_fix = fields.Char(string="Prefix")
    gateway = fields.Char(string="Gateway")
    address_category = fields.Selection(
        [("public", "Public"), ("private", "Private")], string="Address Category"
    )
    vlan_ids = fields.Many2many("isp.vlans", string="VLANS")
