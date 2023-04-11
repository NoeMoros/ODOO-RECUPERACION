from odoo import models, fields, api

class portatil(models.Model):
    
    _name = 'portatil'
    _rec_name = 'modelo'
    _description = 'portatil'
    
    modelo = fields.Char(string='Modelo', required=True)
    marca = fields.Many2one('marca', required=True)
    imagen = fields.Image()
    resolucion = fields.Char(string='Resolución', required=True)
    frecuencia = fields.Integer(string='Frecuencia', required=True)
    tamaño = fields.Char(string='Tamaño', required=True)
    peso = fields.Float(string='Peso', required=True)
    RAM = fields.Integer(string='RAM', required=True)
    HDD = fields.Integer(string='HDD', required=True)
    SSD = fields.Integer(string='SSD', required=True)
    grafica = fields.Char(string='Tarjeta gráfica', required=True)
    USB3 = fields.Integer(string='USB 3.0', required=True)
    USB2 = fields.Integer(string='USB 2.0', required=True)
    placa_base = fields.Char(string='Placa base', required=True)
    lector_discos = fields.Boolean(string='Lector de discos', required=True)
    tactil = fields.Boolean(string='Táctil', required=True)
    tablet = fields.Boolean(string='Tablet', required=True)
    wifi = fields.Boolean(string='Wifi', required=True)
    cable_red = fields.Boolean(string='Conexión por cable', required=True)
    bluetooth = fields.Boolean(string='Bluetooth', required=True)
    HDMI = fields.Boolean(string='HDMI', required=True)
    VGA = fields.Boolean(string='VGA', required=True)
    DPORT = fields.Boolean(string='Display Port', required=True)
    miniDPORT = fields.Boolean(string='mini DPort', required=True)
    thunderbolt = fields.Integer(string='Thunderbolt', required=True)
    jack = fields.Boolean(string='jack 3.5', required=True)
    SIM = fields.Boolean(string='SIM', required=True)
    cantidad = fields.Integer(string='Cantidad', required=True)
    
    productos = fields.One2many('producto', 'portatil')