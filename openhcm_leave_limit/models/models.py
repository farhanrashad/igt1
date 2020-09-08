# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import exceptions
from dateutil import relativedelta
from datetime import date
from datetime import datetime


class HrLeave(models.Model):
    _inherit = 'hr.leave'

    meeting = fields.Char('Meeting type')
    apply = fields.Boolean("Apply Double Validation")
    limit = fields.Boolean("Allow to Override Limit")
    report = fields.Char('Color in Report')

    @api.model
    def create(self, values):
        holiday = super(HrLeave, self).create(values)
        leave_type_id = values.get('holiday_status_id')
        leave_type = self.env['hr.leave.type'].browse(leave_type_id)
        leave_limit_check = leave_type.leave_limit
        allowed_days = leave_type.limit_days
        req_days = values.get('number_of_days')
        # print('allowed_days  ', allowed_days)
        # print('req_days  ', req_days)
        res_user_id = self.env.uid
        emp = self.env['hr.leave'].search([('user_id', '=', res_user_id)])
        # print('emp', emp)
        count = 0
        last_month = 0
        for i in emp:
            if i.state == "validate":
                count = count + i.number_of_days
                last_month = i.date_to.month
        # print('count', count)
        # print('last_month', last_month)
        remaining_days = allowed_days - (count + int(req_days))
        # print('remaining_days', remaining_days)
        date_to = values.get('date_to')
        datetime_object = datetime.strptime(date_to, '%Y-%m-%d %H:%M:%S')
        # print('date_to', date_to)
        # print('datetime_object', datetime_object)
        if leave_limit_check:
            # print('leave_limit_check')
            if remaining_days < 0:
                left_days = req_days - count
                # print('remaining_days')
                if last_month == datetime_object.month or last_month == 0:
                    # print('last_month')
                    msg = ("Your monthly leave limit is :{0} \n You have take {1} leaves in this month\n Now your "
                           "remaining "
                           "leaves are :{2}\n".format(allowed_days, count, left_days))
                    raise exceptions.ValidationError(msg)
        return holiday

    def write(self, values):
        result = super(HrLeave, self).write(values)
        # print("result", result)
        if values.get('date_to') or values.get('holiday_status_id'):
            if values.get('holiday_status_id'):
                # print("1")
                leave_type_id = values.get('holiday_status_id')
                # print("2")
                leave_type = self.env['hr.leave.type'].browse(leave_type_id)
                leave_limit_check = leave_type.leave_limit
                # print("4")
                allowed_days = leave_type.limit_days


            else:
                # print("1.1")
                leave_type_id = self.holiday_status_id.id
                # print("2")
                leave_type = self.env['hr.leave.type'].browse(leave_type_id)
                leave_limit_check = leave_type.leave_limit
                # print("4")
                allowed_days = leave_type.limit_days
                # print("5")

            if values.get('number_of_days'):
                req_days = values.get('number_of_days')
            else:
                req_days = self.number_of_days
            if values.get('date_to'):
                date_to = values.get('date_to')
            else:
                date_to = str(self.date_to)
            # print('req_days', req_days)
            # print("6")
            res_user_id = self.env.uid
            # print("7")
            emp = self.env['hr.leave'].search([('user_id', '=', res_user_id)])
            # print("8")
            count = 0
            # print("9")
            last_month = 0
            # print("0")
            for i in emp:
                # print("11")
                if i.state == "validate":
                    # print("12")
                    count = count + i.number_of_days
                    # print("13")
                    last_month = i.date_to.month

                    # print("14")
            remaining_days = allowed_days - (count + int(req_days))
            # print("15")
            # print(date_to)
            datetime_object = datetime.strptime(date_to, '%Y-%m-%d %H:%M:%S')
            # print(datetime_object)
            # print('allowed_days', allowed_days)
            # print('emp', emp)
            # print('count', count)
            # print('last_month', last_month)
            # print('remaining_days', remaining_days)
            # print('leave_type_id1', leave_type_id)
            # print('leave_limit_check', leave_limit_check)
            if leave_limit_check:
                #  print('18')
                if remaining_days < 0:
                    left_days = allowed_days - count
                    if last_month == datetime_object.month or last_month == 0:
                        # print('last_month')
                        msg = ("Your monthly leave limit is :{0} \n You have take {1} leaves in this month\n Now your "
                               "remaining "
                               "leaves are :{2}\n".format(allowed_days, count, left_days))
                        raise exceptions.ValidationError(msg)
        return result

    def action_approve(self):

        leave_type_id = self.holiday_status_id.id
        leave_type = self.env['hr.leave.type'].browse(leave_type_id)
        leave_limit_check = leave_type.leave_limit
        allowed_days = leave_type.limit_days
        req_days = self.number_of_days
        # print('allowed_days  ', allowed_days)
        # print('req_days  ', req_days)
        res_user_id = self.env.uid
        emp = self.env['hr.leave'].search([('user_id', '=', res_user_id)])
        # print('emp', emp)
        count = 0
        last_month = 0
        for i in emp:
            if i.state == "validate":
                count = count + i.number_of_days
                last_month = i.date_to.month
        # print('count', count)
        # print('last_month', last_month)
        remaining_days = allowed_days - (count + req_days)
        # print('remaining_days', remaining_days)
        date_to = str(self.date_to)
        datetime_object = datetime.strptime(date_to, '%Y-%m-%d %H:%M:%S')
        # print('date_to', date_to)
        # print('datetime_object', datetime_object)
        if leave_limit_check:
            # print('leave_limit_check')
            if remaining_days < 0:
                left_days = allowed_days - count
                # print('remaining_days')
                if last_month == datetime_object.month or last_month == 0:
                    # print('last_month')
                    msg = ("Your monthly leave limit is :{0} \n You have take {1} leaves in this month\n Now your "
                           "remaining "
                           "leaves are :{2}\n".format(allowed_days, count, left_days))
                    raise exceptions.ValidationError(msg)
        rec = super(HrLeave, self).action_approve()
        return rec


class HrLeaveType(models.Model):
    _inherit = 'hr.leave.type'

    leave_limit = fields.Boolean("Monthly Leave Limit")
    limit_days = fields.Float('Leave Limit Days', deafult=13)
