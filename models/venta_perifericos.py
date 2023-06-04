from odoo import models, fields, api

class venta_periferico(models.Model):
    _name = "venta_periferico"
    _rec_name = "nombre"
    _description = "venta_periferico"

    nombre = fields.Char(string="Registro", compute='_dependecias')
    comprador = fields.Many2one('usuario', required=True)
    vendedor = fields.Many2one('usuario', required=True)
    precio = fields.Integer(string='Precio', required=True)
    fecha_venta = fields.Date(string="Fecha de venta", required=True)
    perifericos = fields.Many2one('perifericos', compute='compute_ventas_producto', inverse='ventas_producto_inverse', string='Producto', unique=True, required=True)
    ventas_producto = fields.One2many('perifericos', 'venta')
    devoluciones = fields.One2many('devoluciones', 'venta')

    @api.onchange('perifericos')
    def _onchange_producto(self):
        if self.perifericos:
            self.vendedor = self.producto.vendedor

    def ventas_review_inverse(self):
        if len(self.ventas_review) > 0:
            # delete previous reference
            stage = self.env['post_venta'].browse(self.ventas_review[0].id)
            asset.venta = False
        # set new reference
        self.review.venta = self

    
    @api.depends('ventas_producto')
    def compute_ventas_producto(self):
        if len(self.ventas_producto) > 0:
            self.perifericos = self.ventas_producto[0]

    def ventas_producto_inverse(self):
        if len(self.ventas_producto) > 0:
            # delete previous reference
            stage = self.env['producto'].browse(self.ventas_producto[0].id)
            asset.venta = False
        # set new reference
        self.producto.venta = self
    
    @api.depends('comprador', 'vendedor', 'perifericos', 'fecha_venta', 'precio')
    def _dependecias(self):
        for record in self:
            record.nombre = str(record.comprador.nombre) + ' compro el producto ' + str(record.perifericos) + ' de ' + str(record.vendedor.nombre) + ' por ' + str(record.precio) + '€' + ' el dia ' + str(record.fecha_venta)
   
    @api.onchange('vendedor')
    def _onchange_vendedor(self):
        try:
            if self.vendedor:
                if self.vendedor.vendedor == False:
                    raise ValueError("El usuario no es vendedor")
                else:
                    self.perifericos = self.vendedor.productos[0]
        except:
            return {
                'warning': {
                    'title': "Error",
                    'message': "El usuario no es vendedor",
                }
            }
        
    @api.onchange('perifericos')
    def _onchange_producto(self):
        try:
            if self.perifericos:
                if self.perifericos.venta:
                    raise ValueError("El producto ya ha sido vendido")
                else:
                    self.vendedor = self.producto.vendedor
        except:
            return {
                'warning': {
                    'title': "Error",
                    'message': "El producto ya ha sido vendido",
                }
            }

    @api.onchange('vendedor', 'comprador')
    def _onchange_usuario(self):
        try:
            if self.vendedor and self.comprador:
                if self.vendedor == self.comprador:
                    raise ValueError("No puede comprarse un producto a si mismo")
        except:
            return {
                'warning': {
                    'title': "Error",
                    'message': "No puede comprarse un producto a si mismo",
                }
            }

    @api.onchange('perifericos', 'vendedor')
    def _onchange_producto_vendedor(self):
        try:
            if self.perifericos and self.vendedor:
                if self.perifericos.vendedor != self.vendedor:
                    raise ValueError("El producto no pertenece al vendedor") 
        except:
            return {
                'warning': {
                    'title': "Error",
                    'message': "El producto no pertenece al vendedor",
                }
            }

    @api.onchange('precio')
    def _onchange_precio(self):
        try:
            if self.precio:
                if self.precio <= 0:
                    raise ValueError("El precio no puede ser negativo o gratuito")
        except:
            return {
                'warning': {
                    'title': "Error",
                    'message': "El precio no puede ser negativo o gratuito",
                }
            }