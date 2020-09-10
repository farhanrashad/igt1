# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import datetime
import calendar



class LeaveSummaryWizard(models.Model):
    _name = "leave.summary"
    _description = "Leave Summary Report"
    
    
#     declaring attandance wizard fields
    date_from=fields.Date(string="From",default=datetime.datetime.today(),required=True)
    date_to=fields.Date(string="To",default=datetime.datetime.today(),required=True)
    department=fields.Many2many('hr.department',string="Department")



    def action_report_gen(self):
        print("called action report gen----------------------------")
        #for months report
        date_from=self.date_from
        date_to=self.date_to


        print(type(self.department))
        department_id=[]
        count=0;
        for id in self.department:
            print(self.department[count].id)
            department_id.append(self.department[count].id)
            count += 1
        print(department_id)
        datas = {

            'all_dep': department_id,
            'date_from' : date_from,
            'date_to' : date_to

        }
        return self.env.ref('de_hr_leave_summary.leave_sum_xlsx').report_action(self,data=datas)