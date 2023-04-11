from odoo import models, fields, api

class venta(models.Model):
    _name = "venta"
    _rec_name = "nombre"
    _description = "venta"

    nombre = fields.Char(string="Registro", compute='_dependecias')
    comprador = fields.Many2one('usuario', required=True)
    vendedor = fields.Many2one('usuario', required=True)
    precio = fields.Integer(string='Precio', required=True)
    fecha_venta = fields.Date(string="Fecha de venta", required=True)
    review = fields.Many2one('post_venta', compute='compute_ventas_review', inverse='ventas_review_inverse', string='Review', store=True)
    ventas_review = fields.One2many('post_venta', 'venta')
    producto = fields.Many2one('producto', compute='compute_ventas_producto', inverse='ventas_producto_inverse', string='Producto', unique=True, required=True)
    ventas_producto = fields.One2many('producto', 'venta')

    @api.onchange('producto')
    def _onchange_producto(self):
        if self.producto:
            self.vendedor = self.producto.vendedor

    @api.depends('ventas_review')
    def compute_ventas_review(self):
        if len(self.ventas_review) > 0:
            self.review = self.ventas_review[0]

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
            self.producto = self.ventas_producto[0]

    def ventas_producto_inverse(self):
        if len(self.ventas_producto) > 0:
            # delete previous reference
            stage = self.env['producto'].browse(self.ventas_producto[0].id)
            asset.venta = False
        # set new reference
        self.producto.venta = self
    
    @api.depends('comprador', 'vendedor', 'producto', 'fecha_venta', 'precio')
    def _dependecias(self):
        for record in self:
            record.nombre = str(record.comprador.nombre) + ' compro el producto ' + str(record.producto.portatil) + ' de ' + str(record.vendedor.nombre) + ' por ' + str(record.precio) + '€' + ' el dia ' + str(record.fecha_venta)
   
    @api.onchange('vendedor')
    def _onchange_vendedor(self):
        try:
            if self.vendedor:
                if self.vendedor.vendedor == False:
                    raise ValueError("El usuario no es vendedor")
                else:
                    self.producto = self.vendedor.productos[0]
        except:
            return {
                'warning': {
                    'title': "Error",
                    'message': "El usuario no es vendedor",
                }
            }
        
    @api.onchange('producto')
    def _onchange_producto(self):
        try:
            if self.producto:
                if self.producto.venta:
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

    @api.onchange('producto', 'vendedor')
    def _onchange_producto_vendedor(self):
        try:
            if self.producto and self.vendedor:
                if self.producto.vendedor != self.vendedor:
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