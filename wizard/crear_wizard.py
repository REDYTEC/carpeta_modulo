# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class CrearWizard(models.TransientModel):
    _name = 'crear.wizard'
    _description = 'Crear Usando Wizard'

    cadena_texto = fields.Char(string='Cadena de Texto', required=True)
    numero_puntos_decimales = fields.Float(string='Número Decimal')
    seleccion = fields.Selection([
        ('campo_1', 'Selección 1'),
        ('campo_2', 'Selección 2'),
        ('campo_default', 'Default'),
    ], required=True, default='campo_default')

    def action_create(self):
        vals={
            'cadena_texto': self.cadena_texto,
            'numero_puntos_decimales': self.numero_puntos_decimales,
            'seleccion': self.seleccion
        }
        creacion_rec = self.env['nombre.modulo'].create(vals)
        return {
            'name': _('Crear'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'nombre.modulo',
            'res_id': creacion_rec.id,
        }
