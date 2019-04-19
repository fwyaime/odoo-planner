# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class PolicePlanDay(models.Model):
    _name = 'police.plan.day'

    plan_id = fields.Many2one('police.plan', string="Period Plan")
    date = fields.Date()
    official_holiday = fields.Boolean()
    line_ids = fields.One2many('police.plan.day.line', 'day_id', string="Lines")
