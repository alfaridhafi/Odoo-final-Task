from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TrainingClass(models.Model):
    _name = 'campus_management.training_class'
    _description = 'Training Class'

    Dosen = fields.Char(string='Dosen')
    murid= fields.Char(string='Murid')
    kelas  = fields.Char(string='Jurusan', required=True)
    Gedung = fields.Char(string='Gedung', required=True)
    pelajaran = fields.Char(string='Mata kuliah', required=True)
