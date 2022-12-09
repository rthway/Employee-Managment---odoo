# -*- coding: utf-8 -*-
from odoo import api, fields, models


class employeeLocation(models.Model):
    _name = "employee.location"
    _description = "Employee person is an app to record employee location information"
    location = fields.Char(string='Location Name', required=True)
    note = fields.Text(string='Description')
