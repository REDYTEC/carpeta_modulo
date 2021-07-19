# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class CreateAppointmentWizard(models.TransientModel):
    _name = 'buscar.wizard'
    _description = 'Buscar Wizard'

    cadena_texto = fields.Many2one('nombre.modulo', string='Cadena', required=True)

    def action_search_m1(self):
        action = self.env["ir.actions.act_window"]._for_xml_id("carpeta_modulo.action_nombre_modulo")
        action['domain'] = [('cadena_texto', '=', self.cadena_texto.id)]
        return action

    def action_search_m2(self):
        action = self.env.ref('carpeta_modulo.action_nombre_modulo').read()[0]
        action['domain'] = [('cadena_texto', '=', self.cadena_texto.id)]
        return action

    def action_search_m3(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Modulo',
            'res_model': 'nombre.modulo',
            'view_type': 'form',
            'domain': [('cadena_texto', '=', self.cadena_texto.id)],
            'view_mode': 'tree,form',
            'target': 'current',
        }
