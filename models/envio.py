from odoo import _, models, fields, api

class Envio(models.Model):

    _name = 'envio'
    _rec_name = 'venta'
    _description = 'envio'

    venta = fields.Many2one('venta', string='venta', unique=True)
    origen = fields.Char(string="origen", required=True)
    destino = fields.Char(string="destino", required=True)
    estado = fields.Selection([('0', 'Pago Aceptado'), ('1', 'En Preparacion'), ('2', 'En Reparto'), ('3', 'Pedido Recogido')], string='Estado del envio', required=True)
    compañia = fields.Char(string="compañia", required=True)