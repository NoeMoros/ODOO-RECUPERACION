from odoo import models, fields, api

class usuario(models.Model):
    _name = "usuario"
    _rec_name = "nombre"
    _description = "usuario"

    dni = fields.Char(string='DNI', size=9, required=True)
    nombre = fields.Char(string='Nombre', required=True)
    imagen = fields.Image()
    telefono = fields.Char(string='Número de telefono', size=9, required=True)
    email = fields.Char(string='Correo', required=True) 
    producto = fields.One2many('producto', 'vendedor', string='producto a la venta')
    venta = fields.One2many('venta', 'vendedor', string='ventas')
    vendedor = fields.Boolean(string='Vendedor', compute='_vendedor')
    reviews = fields.One2many('post_venta', 'vendedor', string='Reviews')
    compras = fields.One2many('venta', 'comprador', string='Compras')
    chats = fields.Many2many('chat', string='Chats')
    
    @api.depends('producto')
    def _vendedor(self):
        for record in self:
            if len(record.producto) > 0:
                record.vendedor = True
            else:
                record.vendedor = False

    @api.onchange('dni')
    def _onchange_dni(self):
        if self.dni:
            try:
                if len(self.dni) != 9:
                    raise ValueError("El DNI debe tener 9 caracteres")
            except:
                return {
                    'warning': {
                        'title': "Error",
                        'message': "El DNI debe tener 9 caracteres",
                    }
                }
            try:
                if self.dni[8].isalpha() == False:
                    raise ValueError("El último caracter del DNI debe ser una letra")
            except:
                return {
                    'warning': {
                        'title': "Error",
                        'message': "El último caracter del DNI debe ser una letra",
                    }
                }

    @api.onchange('email')
    def _onchange_email(self):
        try:
            if self.email:
                if '@' not in self.email:
                    raise ValueError("El email debe tener un @")
        except:
            return {
                'warning': {
                    'title': "Error",
                    'message': "El email debe tener un @",
                }
            }