# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import calendar
from odoo.exceptions import UserError
from datetime import date, timedelta, datetime
from dateutil import relativedelta


class AccountMove(models.Model):
    _inherit = 'account.move'

    is_appointment_invoice = fields.Boolean(string='Is Appointment Invoice')

