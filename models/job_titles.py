# -*- coding: utf-8 -*-
from odoo import api, fields, models


class employeeJobs(models.Model):
    _name = "employee.jobs"
    _description = "Employee person is an app to record employee jobs title information"
    jobs_title = fields.Char(string='Job Title', required=True)
    note = fields.Text(string='Description')
