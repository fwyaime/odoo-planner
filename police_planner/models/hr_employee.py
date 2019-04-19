# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    police_house_id = fields.Many2one('police.house', string="Police House")

    work_organization = fields.Selection([('fulltime', 'Full-Time'), ('4_days', '4 days a week')])
    free_week_day = fields.Selection([('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday')])
    intervention_type_ids = fields.Many2many('police.intervention.type')

    plan_line_ids = fields.Many2many('police.plan.day.line')

    period_start_consecutive_worked_days = fields.Integer()
    period_start_consecutive_worked_nights = fields.Integer()

    annual_worked_weekends = fields.Integer()
    annual_worked_night_hours = fields.Integer()

    ok_weekends = fields.Boolean()
    ok_nights = fields.Boolean()
    ok_other_genre = fields.Boolean(default=True)
    ok_wednesday_afternoon = fields.Boolean()
    ok_night = fields.Boolean()
    ok_early_morning = fields.Boolean()
