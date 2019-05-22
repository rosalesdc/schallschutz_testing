# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class QualityCheckM(models.Model):
    _inherit = 'mrp.production'

#    quality_point_id = fields.Many2one(
#                                       'quality.point',
#                                       string="Puntos de Control",
#                                       )
#    norma = fields.Float(string='Norma',
#                         related='quality_point_id.norm')
