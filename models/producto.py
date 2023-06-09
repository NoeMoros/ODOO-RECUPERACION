from odoo import models, fields, api

class Producto(models.Model):
    _name = "producto"
    _rec_name = "portatil"
    _description = "Producto"

    portatil = fields.Many2one('portatil', string='Portátil', requiered=True)
    precio = fields.Integer(string='Precio del producto', required=True)
    estado = fields.Selection([
        ('0', 'Recién Fabricado'),
        ('1', 'Casi Nuevo'),
        ('2', 'Algo Desgastado'),
        ('3', 'Bastante Desgastado'),
        ('4', 'Deplorable')
    ], string='Estado del producto', required=True)
    SO = fields.Selection([
        ('0', 'Windows'),
        ('1', 'Linux'),
        ('2', 'Mac'),
    ], string='SO', required=True)
    fechaSubida = fields.Date(string='Fecha de subida')
    vendedor = fields.Many2one('usuario', required=True)
    comprador= fields.Many2one('usuario')
    venta = fields.Many2one('venta', string='Venta')
