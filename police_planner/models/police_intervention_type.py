# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class PoliceInterventionType(models.Model):
    _name = 'police.intervention.type'

    name = fields.Char("Name")
    is_night = fields.Boolean(default=False)
    code = fields.Char()
    start_hour = fields.Float()
    end_hour = fields.Float()
    
