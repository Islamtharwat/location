# -*- coding: utf-8 -*-
#  Copyright (c) 2019.  Coded and Maintained By Eslam Tharwat

from odoo import models, fields, api, _
import requests


class locationx(models.Model):
    _name = "meeting.location"
    _rec_name = 'customer'

    lat_ip = fields.Char(string="Latitude")
    lon_ip = fields.Char(string="Logtude")
    add_ip = fields.Text(string="Address")
    check_in_attendance = fields.Datetime(string="Meeting Start")
    check_out_attendance = fields.Datetime(string="Meeting End")
    customer = fields.Many2one('res.partner', string='Meeting With')
    attendance_meeting = fields.Selection([('attendance', 'Attendance'), ('meeting', 'Meeting')], default="attendance")

    @api.constrains('lat_ip')
    def onchange_location(self):
        self.check_in_attendance = self.env['hr.attendance'].search([])[0].check_in
        self.check_out_attendance = self.env['hr.attendance'].search([])[0].check_out

        x = str(self.lat_ip)
        y = str(self.lon_ip)
        z = ','
        google_api = str(self.env['res.config.settings'].search([])[-1].google_api_key)
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng='+x+z+y+'&key='+google_api)
        request_status = response.json()['status']
        if request_status == 'OK':
            self.add_ip = response.json()['results'][1]['formatted_address']
            print(request_status)
        else:
            self.add_ip = False
            print(request_status)
            
    def _default_employee(self):
        return self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)

    employee_id = fields.Many2one('hr.employee', string="Employee", default=_default_employee, ondelete='cascade', index=True)

    @api.onchange('attendance_meeting')
    def onchange_customer(self):
        if self.attendance_meeting == 'attendance':
            self.customer = False
