from odoo import models, fields

class StudentProfile(models.Model):
    _name = 'student.profile'
    _inherits = {'res.partner': 'partner_id'}  # Delegation

    partner_id = fields.Many2one('res.partner', required=True, ondelete='cascade')
    student_id = fields.Char(string="Student ID")
