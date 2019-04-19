# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class PolicePlanDayLine(models.Model):
    _name = 'police.plan.day.line'

    day_id = fields.Many2one('police.plan.day', string="Day")

    intervention_type = fields.Many2one('police.intervention.type')

    name = fields.Char(related='intervention_type.name')
    start_hour = fields.Float(related='intervention_type.start_hour')
    end_hour = fields.Float(related='intervention_type.end_hour')
    is_night = fields.Boolean(related='intervention_type.is_night')

    employee_ids = fields.Many2many('hr.employee')

    state = fields.Selection([('draft', 'Draft'), ('error', 'Error'), ('confirmed', 'Confirmed')], default='draft')

    error_reason = fields.Char()
    
