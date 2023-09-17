# -*- coding: utf-8 -*-
from odoo import _, models, fields, api
from odoo.fields import Date


class CalendarEvent(models.Model):
    _inherit = "calendar.event"

    appointment_invoice_count = fields.Integer("Invoice", compute='_compute_appointment_invoice_count')

    @api.depends()
    def _compute_appointment_invoice_count(self):
        for rec in self:
            appointment_invoices = self.env['account.move'].sudo().search(
                [('partner_id', 'in',  self.partner_ids.ids), ('is_appointment_invoice', '=', True)])
            rec.appointment_invoice_count = len(appointment_invoices)

    def create_appointment_invoice(self):
        journal_id = self.env['account.journal'].search([('type', '=', 'sale')], limit=1)
        # Find the "Appointment Fees" product by name
        product = self.env['product.product'].search([('name', '=', 'Appointment Fees')], limit=1)
        if not product:
            # Create the product if it doesn't exist
            product = self.env['product.product'].create({
                'name': 'Appointment Fees',
                'type': 'service',  # Set the appropriate product type
                'list_price': 200.00,  # Set the default list price
            })

        line_vals = {
            'name': 'Appointment fees',
            'product_id': product.id,  # Set the product as the invoice line's product
            'quantity': 1,
            'price_unit': product.list_price,  # Use the product's list price
        }
        move_vals = {
            'date': Date.today(),
            'ref': 'Appointment Fees',
            'move_type': 'out_invoice',
            'journal_id': journal_id.id,
            'currency_id': journal_id.currency_id.id or self.env.company.currency_id.id,
            'partner_id': self.partner_ids.ids.pop(),
            'is_appointment_invoice': True,
            'invoice_line_ids': [(0, 0, line_vals)]
        }
        self.env['account.move'].create(move_vals)

    def action_view_appointment_invoice(self):
        appointment_invoices = self.env['account.move'].sudo().search(
            [('partner_id', 'in',  self.partner_ids.ids), ('is_appointment_invoice', '=', True)])
        action = self.env.ref('account.action_move_out_invoice_type').read()[0]
        if len(appointment_invoices) > 1:
            action['domain'] = [('id', 'in', appointment_invoices.ids)]
        elif len(appointment_invoices) == 1:
            action['views'] = [(self.env.ref('account.view_move_form').id, 'form')]
            action['res_id'] = appointment_invoices.ids[0]
        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action

