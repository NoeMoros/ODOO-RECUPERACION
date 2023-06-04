from odoo import models, fields, api

class perifericos(models.Model):
    _name = 'perifericos'
    _rec_name = 'periferico'
    _description = 'venta periferico'
    
    periferico = fields.Many2one('periferico', string='Periferico', requiered=True)
    precio = fields.Integer(string='Precio del producto', required=True)
    estado = fields.Selection([
        ('0', 'Recién Fabricado'),
        ('1', 'Casi Nuevo'),
        ('2', 'Algo Desgastado'),
        ('3', 'Bastante Desgastado'),
        ('4', 'Deplorable')
    ], string='Estado del producto', required=True)
    fechaSubida = fields.Date(string='Fecha de subida')
    vendedor = fields.Many2one('usuario', required=True)
    venta = fields.Many2one('venta_periferico', string='Venta')
