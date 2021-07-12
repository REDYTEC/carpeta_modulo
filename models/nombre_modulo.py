# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, tools


class NombreClase(models.Model):
    _name = "nombre.modulo"
    _description = "Nombre Modulo"

    name = fields.Char(string='Secuencia', copy=False, readonly=True, required=True,
                       default=lambda self: _('New'))
    cadena_texto = fields.Char(string='Cadena de Texto')
    numero_entero = fields.Integer(string='Número Entero')
    numero_puntos_decimales = fields.Float(string='Número Decimal')
    variable_boleana = fields.Boolean(strin='Variable Boleana')
    texto_largo = fields.Text(string='Texto Largo / Notas')
    seleccion = fields.Selection([
        ('campo_1', 'Selección 1'),
        ('campo_2', 'Selección 2'),
    ])
    fecha = fields.Date(string='Fecha')
    fecha_y_hora = fields.Datetime(string='Fecha Y Hora')

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('nombre.modulo') or _('New')
        return super(NombreClase, self).create(vals)
