from odoo import models, fields, api

class Devolucion(models.Model):
    _name = 'devolucion'
    _description = 'Devoluciones'

    venta = fields.Many2one('venta', string='Venta Original', required=True)
    fecha_devolucion = fields.Date(string='Fecha de Devolución', default=fields.Date.today(), required=True)
    motivo_devolucion = fields.Char(string='Motivo de Devolución', required=True)

    @api.model_create_single
    def eliminar_registro_venta(self):
        venta = self.venta
        if venta:
            venta.unlink()
            return True
        else:
            return False

