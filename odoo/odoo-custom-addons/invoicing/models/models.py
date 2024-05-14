# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Invoicing(models.Model):
    _name = 'invoicing.invoicing'
    _description = 'Invoices'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    customer_id = fields.Many2one('res.partner', string='Customer')
    expiration_date = fields.Date(string='Expiration Date')
    quotation_date = fields.Date(string='Quotation Date')
    payment_terms = fields.Selection([
        ('immediate', 'Immediate Payment'),
        ('10_days', 'Within 10 Days'),
        ('15_days', 'Within 15 Days'),
        ('21_days', 'Within 21 Days'),
        ('end_of_month', 'end of the following Month')
    ], string='Payment Terms')

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

