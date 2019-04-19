# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class PolicePlan(models.Model):
    _name = 'police.plan'

    start_date = fields.Date("Start Date")
    end_date = fields.Date("End Date")
    house_id = fields.Many2one('police.house', string="House")
    day_ids = fields.One2many('police.plan.day', 'plan_id', string="Days")

    state = fields.Selection([('draft', 'Draft'), ('error', 'Error'), ('confirmed', 'Confirmed'), ('cancel', 'Cancelled')], default='draft')

    planner_result = fields.Selection([('a', 'OK for all'), ('b', 'OK for obligations and some wishes'), ('c', 'OK only for obligations'), ('d', 'Impossible to match all obligations')])
