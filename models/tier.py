# -*- coding: utf-8 -*-
from odoo import api, fields, models


class employeeTier(models.Model):
    _name = "employee.tier"
    _description = "Employee person is an app to record employee tier information"
    tier = fields.Char(string='Tier Name', required=True)
    note = fields.Text(string='Description')