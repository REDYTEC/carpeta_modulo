# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, tools


class NombreClase(models.Model):
    _name = "nombre.modulo"
    _description = "Nombre Modulo"
    _rec_name = "cadena_texto"

    name = fields.Char(string='Secuencia', copy=False, readonly=True, required=True,
                       default=lambda self: _('New'))
    cadena_texto = fields.Char(string='Cadena de Texto', required=True)
    numero_entero = fields.Integer(string='Número Entero', readonly=True, default=8)
    numero_puntos_decimales = fields.Float(string='Número Decimal')
    variable_boleana = fields.Boolean(strin='Variable Boleana')
    uno = fields.Boolean(string='Este Mejor')
    dos = fields.Boolean(string='Mejor Este')
    notas = fields.Text(string='Notas Extra')
    texto_largo = fields.Text(string='Texto Largo / Notas')
    seleccion = fields.Selection([
        ('campo_1', 'Selección 1'),
        ('campo_2', 'Selección 2'),
        ('campo_default', 'Default'),
    ], required=True, default='campo_default')
    fecha = fields.Date(string='Fecha')
    fecha_y_hora = fields.Datetime(string='Fecha Y Hora')
    state = fields.Selection([('draft', 'Borrador'), ('confirm', 'Confirmado'),
                              ('done', 'Hecho'), ('cancel', 'Cancelado')], default='draft',
                             string='Status')
    image = fields.Binary(string='Doctor Image')

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('nombre.modulo') or _('New')
        return super(NombreClase, self).create(vals)
