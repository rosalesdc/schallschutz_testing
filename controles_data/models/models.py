# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class QualityCheckM(models.Model):
    _inherit = 'quality.check'

    quality_point_id = fields.Many2one(
                                       'quality.point',
                                       string="Puntos de Control",
                                       )
    norma = fields.Float(string='Norma',
                         related='quality_point_id.norm')
    
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100