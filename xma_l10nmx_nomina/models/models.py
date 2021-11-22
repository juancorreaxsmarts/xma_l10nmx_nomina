# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, models, fields


class TmsResPartners(models.Model):
    _inherit = 'hr.employee'


#Fonacot
    saldo_fonacot = fields.Float()
    monto_descuento = fields.Float()

#Prestamos
    saldo_prestamo = fields.Float()
    monto_periodico = fields.Float()

#Pension Alimenticia
    pension_alimenticia = fields.Boolean()
    porcentaje_pension = fields.Float()

# Despensa
    porcentaje_despensa = fields.Float()
