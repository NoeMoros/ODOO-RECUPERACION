from odoo import models, fields, api

class DevolucionPeriferico(models.Model):
    _name = 'devoluciones'
    _description = 'devolucionesPeriferico'

    venta = fields.Many2one('venta_periferico', string='Venta Original', required=True)
    fecha_devolucion = fields.Date(string='Fecha de Devolución', default=fields.Date.today(), required=True)
    motivo_devolucion = fields.Char(string='Motivo de Devolución', required=True)

    @api.depends('venta')
    def eliminar_registro_venta(self):
        venta = self.venta
        if venta:
            venta.unlink()
            return True
        else:
            return False

