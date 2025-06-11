from odoo import models, fields


class StudentRecord(models.Model):
    _name ="student.record"
    _description=" Student records"

    name=fields.Char(string="Name",required=True,help="Strudent name")
    address=fields.Char(string="Address",required=True,help="Student address")
    phone=fields.Char(string="Phone",help="contact number")
    email=fields.Char(string="Email",help="email address")
