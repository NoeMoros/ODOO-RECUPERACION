from odoo import _, api, fields, models
from odoo.exceptions import *

class Mensaje(models.Model):

    _name = 'mensaje'
    _rec_name = 'texto'
    _description = 'mensaje'

    texto = fields.Char(string="Texto", required=True)
    fecha = fields.Datetime(string="Fecha y hora", required=True)
    chat = fields.Many2one('chat', string='Chat', required=True)
    usuario = fields.Many2one('usuario', string='Usuario', required=True, domain="[('chats', 'in', chat)]")
