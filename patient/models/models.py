# -*- coding: utf-8 -*-

from odoo import models, fields, api


class patient(models.Model):
    _name = 'patient.patient'
    _description = 'patient.patient'

    name = fields.Char()
    middle_name = fields.Char()
    last_name = fields.Char()
    dob = fields.Date(string="Date of birth", default=fields.Date.context_today, required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ('unspecified', 'Unspecified'),
        ], string="Gender", default='unspecified')
    nationality_id = fields.Many2one('res.country', string='Nationality')
    martial_status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('civil partnered', 'Civil Partnered'),
        ('widowed', 'Widowed'),
        ('divorced', 'Divorced'),
        ('separated', 'Separated')
    ])
    