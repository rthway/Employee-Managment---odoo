# -*- coding: utf-8 -*-
from odoo import api, fields, models


class employeeDivision(models.Model):
    _name = "employee.division"
    _description = "Employee person is an app to record employee division information"
    division = fields.Char(string='Division Name', required=True)
    note = fields.Text(string='Description')