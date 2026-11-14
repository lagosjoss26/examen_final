from odoo import api, fields, models
from odoo.exceptions import ValidationError

class BibliotecaPrestamo(models.Model):
    _name = "unicah.prestamo"
    _description = "Préstamo de libro"

    name = fields.Char(string="Libro", required=True)
    estudiante_id = fields.Many2one("res.partner", string="Estudiante", required=True)
    fecha_prestamo = fields.Date(string="Fecha préstamo", required=True, default=fields.Date.context_today)
    fecha_devolucion = fields.Date(string="Fecha devolución", required=True)
    dias_prestamo = fields.Integer(string="Días de préstamo", compute="_compute_dias", store=True)
    estado = fields.Selection(
        [
            ("prestado", "Prestado"),
            ("devuelto", "Devuelto"),
        ],
        string="Estado",
        default="prestado",
    )

    @api.depends("fecha_prestamo", "fecha_devolucion")
    def _compute_dias(self):
        for rec in self:
            if rec.fecha_prestamo and rec.fecha_devolucion:
                rec.dias_prestamo = (rec.fecha_devolucion - rec.fecha_prestamo).days
            else:
                rec.dias_prestamo = 0

    @api.constrains("fecha_prestamo", "fecha_devolucion")
    def _check_fechas(self):
        for rec in self:
            if rec.fecha_prestamo and rec.fecha_devolucion:
                if rec.fecha_devolucion < rec.fecha_prestamo:
                    raise ValidationError("La fecha de devolución no puede ser antes que la fecha de préstamo.")