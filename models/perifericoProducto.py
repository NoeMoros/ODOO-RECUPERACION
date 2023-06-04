from odoo import models, fields, api

class perifericoProducto(models.Model):
    _name = "ventaPerifericos"
    _rec_name="perifericoProducto"
    _description = "Periferico producto"

    perifericoProducto = fields.Many2one('periferico', string='Periferico')
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

    venta = fields.Many2one('venta', string='Venta')
