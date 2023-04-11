from odoo import _, models, fields, api

class Marca(models.Model):

    _name = 'marca'
    _rec_name = 'nombre'
    _description = 'marca de portatil'

    nombre = fields.Char(string='nombre', required=True)