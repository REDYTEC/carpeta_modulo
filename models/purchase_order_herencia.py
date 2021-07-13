# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    referencia_modulo = fields.Many2one('nombre.modulo', string='Referencia Módulo')
