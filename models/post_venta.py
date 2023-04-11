from odoo import models, fields, api

class post_venta(models.Model):

    _name = 'post_venta'
    _rec_name='mensaje'
    _description = 'post_venta'

    puntuacionDada = fields.Integer(string="Puntuación (1 - 5)", required=True)
    vendedor = fields.Many2one('usuario', string='Vendedor', readonly=True, required=True)
    mensaje = fields.Char(string="mensaje")
    venta = fields.Many2one('venta', string='Venta', required=True)

    @api.onchange('puntuacionDada')
    def _onchange_puntuacionDada(self):
        try:
            if self.puntuacionDada:
                if self.puntuacionDada < 1 or self.puntuacionDada > 5:
                    raise ValueError("La puntuación debe estar entre 1 y 5")
        except:
            return {
                'warning': {
                    'title': "Error",
                    'message': "La puntuación debe estar entre 1 y 5",
                }
            }

    @api.onchange('venta')
    def _onchange_venta(self):
        if self.venta:
            self.vendedor = self.venta[0].vendedor

