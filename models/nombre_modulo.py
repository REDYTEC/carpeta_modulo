# -*- coding: utf-8 -*-
# esto primero es forzoso
from odoo import api, fields, models, _, tools


class NombreClase(models.Model):
    _name = "nombre.modulo"
    _description = "Nombre Modulo"

    cadena_texto = fields.Char(string='Nombre Visible en Menú')
    numero_entero = fields.Integer(string='Nombre Visible en Menú')
    numero_puntos_decimales = field.Float(string='Nombre Visible en Menú')
    variable_boleana = field.Boolean(strin='Nombre Visible en Menú')
    texto_largo = field.Text(string='Nombre Visible en Menú')
    seleccion = field.Selection([
        ('campo_1', 'Nombre en Menú 1'),
        ('campo_2', 'Nombre en Menú 2'),
    ])
    fecha = fields.Date(string='Nombre en Menú')
    fecha_y_hora = fields.Datetime(string='Nombre en Menú')