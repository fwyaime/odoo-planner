# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class PoliceZone(models.Model):
    _name = "police.zone"

    name = fields.Char("Name")
    house_ids = fields.One2many('police.house', 'zone_id', string="Police Houses")

    # Rules for this zone
    employee_hours_per_week = fields.Integer()
    employee_days_per_week = fields.Integer()

    employee_hours_per_day = fields.Float()

    
