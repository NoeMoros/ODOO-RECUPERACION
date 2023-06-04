from odoo import models, fields, api

class Periferico(models.Model):
    _name = 'periferico'
    _rec_name = 'periferico'
    _description = 'periferico'
    
    periferico = fields.Char(string="Periferico", required=True)
    modelo = fields.Char(string='Modelo', required=True)
    marca = fields.Many2one('marca', required=True)
    imagen = fields.Image()
    estado = fields.Selection([('0', 'Recién Fabricado'), ('1', 'Casi Nuevo'), ('2', 'Algo Desgastado'), ('3', 'Bastante Desgastado'), ('4', 'Deplorable')], string='Estado del producto', required=True)
    precio = fields.Integer(string='Precio del producto', required=True)
    productos = fields.One2many('perifericos', 'periferico')