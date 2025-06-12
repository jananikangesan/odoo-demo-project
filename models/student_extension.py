from odoo import models, fields

class StudentRecordExtended(models.Model):
    _inherit = 'student.record'

    date_of_birth = fields.Date(string="Date of Birth", help="Student's date of birth")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender")
