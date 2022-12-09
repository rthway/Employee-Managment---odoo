# -*- coding: utf-8 -*-
from odoo import api, fields, models


class employeeDepartment(models.Model):
    _name = "employee.department"
    _description = "Employee person is an app to record employee department information"
    department = fields.Char(string='Department Name', required=True)
    note = fields.Text(string='Description')
