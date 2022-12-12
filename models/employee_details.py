# -*- coding: utf-8 -*-
from odoo import api, fields, models


class employeeDetails(models.Model):
    _name = "employee.details"
    _description = "Employee person is an app to record employee personal information"
    _inherit="employee.person"
    person=fields.Many2one('employee.person') 