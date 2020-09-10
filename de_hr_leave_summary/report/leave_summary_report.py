import xlwt

from odoo import models
import datetime

class PartnerXlsx(models.AbstractModel):
    _name = 'report.de_hr_leave_summary.report_leave_sum_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
            date_from=data['date_from']
            date_to=data['date_to']
            print(data['all_dep'],type(data['all_dep']))
            sheet = workbook.add_worksheet("Leave Summary Report")
            bold = workbook.add_format({'bold': True})
            sheet.set_column('G:G', 22)
            sheet.write('G1', "Leave Summary Report", bold)
            # gave to and from date to report

            print("date from  is : ",data['date_from'],"\nType is :",type(data['date_from']))
            sheet.set_column('F:F', 10)
            sheet.write('F3',date_from, bold)
            sheet.write('G3',"To", bold)
            sheet.set_column('H:H', 10)
            sheet.write('H3', date_to, bold)

            # giving headers for report

            sheet.set_column('D:D', 10)
            sheet.write('D5',"Date", bold)
            sheet.set_column('E:E', 10)
            sheet.write('E5',"No of Days", bold)

            sheet.set_column('F:F', 16)
            sheet.write('F5', "Employee", bold)
            sheet.write('G5', "Department", bold)
            sheet.write('H5', "Leave Type", bold)
            sheet.set_column('I:I', 24)
            sheet.write('I5', "Description", bold)
            sheet.set_column('J:J', 10)
            sheet.write('J5', "End Date", bold)

            department_ids=data['all_dep']
            # generating list for date from to To
            i = 0
            date_str = str(data['date_from'])
            date_to = str(data['date_to'])
            # date_object = datetime.strptime(date_str, '%Y-%m-%d').date()
            date_object = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            date_object_to = datetime.datetime.strptime(date_to, '%Y-%m-%d').date()
            print(type(date_object))
            print("From : ", date_object, "  To : ", date_object_to)
            date_lst=[]
            emp_leave_sum={}
            # print(date_object)  # printed in default formatting
            for y in range(1000000):
                    print(date_object_to - datetime.timedelta(i))
                    date_lst.append(date_object_to - datetime.timedelta(i))
                    if date_object_to - datetime.timedelta(i) == date_object:
                            break;
                    i += 1
            print(date_lst,type(date_lst),type(date_lst[0]));
#             looping all date range
            row=6
            width=3
            for leave_date in date_lst:
                    leave_emp = self.env['hr.leave'].search([('request_date_from', '=',leave_date)])
                    print(leave_emp,type(leave_emp))
#                     if multiple emp were taking leave that day

                    count=0;
                    for single_emp in leave_emp:
                            if len(department_ids) == 0 :
                                    sheet.write(row,width,str(leave_emp[count].request_date_from))
                                    sheet.write(row,width+1,leave_emp[count].number_of_days)
                                    sheet.write(row,width+2,leave_emp[count].employee_id[0].name)
                                    sheet.write(row,width+3,leave_emp[count].department_id[0].name)
                                    sheet.write(row,width+4,leave_emp[count].holiday_type)
                                    sheet.write(row,width+5,leave_emp[count].name)
                                    sheet.write(row,width+6,str(leave_emp[count].request_date_to))
                                    emp_id=int(leave_emp[count].employee_id[0].id)
                                    emp_days=float(leave_emp[count].number_of_days)
                                    if emp_id in emp_leave_sum:
                                            emp_leave_sum[emp_id]=emp_leave_sum.get(emp_id)+emp_days
                                            row += 1
                                            continue;
                                    emp_leave_sum[emp_id]=emp_days
                                    row += 1
                            elif len(department_ids) > 0: #means user selects a department or departments
                                     #to check user selected department ids
                                    dep_count=0
                                    for dep in department_ids:
                                            if department_ids[dep_count] == leave_emp[count].department_id[0].id:
                                                    sheet.write(row, width, str(leave_emp[count].request_date_from))
                                                    sheet.write(row, width + 1, leave_emp[count].number_of_days)
                                                    sheet.write(row, width + 2, leave_emp[count].employee_id[0].name)
                                                    sheet.write(row, width + 3, leave_emp[count].department_id[0].name)
                                                    sheet.write(row, width + 4, leave_emp[count].holiday_type)
                                                    sheet.write(row, width + 5, leave_emp[count].name)
                                                    sheet.write(row, width + 6, str(leave_emp[count].request_date_to))
                                                    emp_id = int(leave_emp[count].employee_id[0].id)
                                                    emp_days = float(leave_emp[count].number_of_days)
                                                    if emp_id in emp_leave_sum:
                                                            emp_leave_sum[emp_id] = emp_leave_sum.get(emp_id) + emp_days
                                                            row += 1
                                                            dep_count += 1
                                                            continue;
                                                    emp_leave_sum[emp_id] = emp_days
                                                    row += 1
                                            dep_count += 1

                            count += 1

            print(emp_leave_sum)
            sheet2 = workbook.add_worksheet("Employee Wise Leave Summary")
            sheet2.set_column('G:G', 30)
            sheet2.write('G1', "Employee Wise Leave Summary", bold)
            sheet2.set_column('F:F', 16)
            sheet2.write('F3',str(date_from), bold)
            sheet2.write('G3',"To", bold)
            sheet2.set_column('H:H', 16)
            sheet2.write('H3',str(date_to), bold)
               #for Employee header
            sheet2.write('F5',"Employee", bold)
            sheet2.write('H5',"No Of Leaves", bold)
            #don printing header
            row = 6
            width = 5
            for e_id in emp_leave_sum:
                    emp_name = self.env['hr.employee'].search([('id', '=', e_id)])
                    sheet2.write(row,width,emp_name[0].name)
                    sheet2.write(row,width+2,emp_leave_sum[e_id])
                    row += 1










