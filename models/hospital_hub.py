# -*- coding: utf-8 -*-
from odoo import api, fields, models


class employeehospitalhub(models.Model):
    _name = "employee.hospitalhub"
    _description = "Employee person is an app to record employee hospital Hub information"
    hospitalhub = fields.Char(string='Hospital Hub Name', required=True)
    note = fields.Text(string='Description')