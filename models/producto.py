from odoo import models, fields, api

class producto(models.Model):

    _name = "producto"
    _rec_name = "portatil"
    _description = "producto"
    tipo_producto=fields.Boolean(string="Es un periferico o un portatil", default=False)
    portatil = fields.Many2one('portatil', string='Portatil')
    periferico=fields.Many2one('periferico', string="periferico")
    precio = fields.Integer(string='Precio del producto', required=True)
    estado = fields.Selection([('0', 'Recién Fabricado'), ('1', 'Casi Nuevo'), ('2', 'Algo Desgastado'), ('3', 'Bastante Desgastado'), ('4', 'Deplorable')], string='Estado del producto', required=True)
    fechaSubida = fields.Date(string='Fecha de subida')
    vendedor = fields.Many2one('usuario', required=True)
    venta = fields.Many2one('venta', string='Venta')
    
