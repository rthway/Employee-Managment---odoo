# -*- coding: utf-8 -*-
from odoo import api, fields, models


class employeeDetails(models.Model):
    _name = "employee.details"
    _description = "Employee details is an app to record employee full information" 
    person = fields.Many2one('employee.person',"Responsible") 
    hire_date = fields.Date(string="Hire Date", required=True)
    resign_date = fields.Date(string="Resign Date")
