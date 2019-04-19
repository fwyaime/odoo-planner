# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class PoliceHouse(models.Model):
    _name = 'police.house'

    name = fields.Char("Name")
    code = fields.Char()
    zone_id = fields.Many2one('police.zone', string="Police Zone")
    employee_ids = fields.One2many('hr.employee', 'police_house_id', string="Employees")
    period_plan_ids = fields.One2many('police.plan', 'house_id', string="Plans")

    parent_house_id = fields.Many2one('police.house', string="Parent")
