# -*- coding: utf-8 -*-

from odoo import models, fields, api


class patient(models.Model):
    _name = 'patient.patient'
    _description = 'patient.patient'

    name = fields.Char()
    middle_name = fields.Char()
