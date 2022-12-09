# -*- coding: utf-8 -*-
from odoo import api, fields, models


class employeePerson(models.Model):
    _name = "employee.person"
    _description = "Employee person is an app to record employee personal information"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ], required=True, default='Male')
    address = fields.Char(string='Address', required=True)
    email=fields.Char(string='Email', required=True)
    phone = fields.Integer(string='Phone No')
    note = fields.Text(string='Description')
