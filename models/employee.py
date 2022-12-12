# -*- coding: utf-8 -*-
from odoo import api, fields, models


class employeeEmployee(models.Model):
    _name = "employee.employee"
    _description = "Employee person is an app to record employee  information"
    person = fields.many2one('employee.person',string="Person")
