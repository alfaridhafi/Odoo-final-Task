from odoo import api,models,fields

class Pelajaran(models.Model):
    _name = "campus_management.pelajaran"
    _description = "Mata kuliah"
    _rec_name = 'pelajaran'

    pelajaran = fields.Char(string="Mata kuliah")

