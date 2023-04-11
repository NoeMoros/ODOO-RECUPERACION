from odoo import _, models, fields, api

class Chat(models.Model):

    _name = "chat"
    _rec_name="name"
    _description = "chat"

    name = fields.Char(string="Chat", compute='_compute_name', store=True)
    usuarios = fields.Many2many('usuario', string='Destinatarios')
    mensajes = fields.One2many('mensaje', 'chat', string='Mensajes')

    @api.depends('usuarios', 'mensajes')
    def _compute_name(self):
        for record in self:
            record.name = ""
            for usuario in record.usuarios:
                record.name += usuario.nombre + ", "
            record.name = record.name[:-2]
            if len(record.mensajes) > 0:
                record.name += ": " + record.mensajes[-1].texto