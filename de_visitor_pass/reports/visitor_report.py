from odoo import tools
from odoo import api, fields, models
import datetime


class SaleReport(models.Model):
    _name = "visitor.report"
    _description = "Visitor Report"

    count=fields.Integer(string="Count")
    check_in=fields.Many2one("visit.detail",string="Check In")
    check_out=fields.Many2one("visit.detail",string="Check Out")
    total_duration=fields.Date(string="Total Duration",default="_get_total_duration")


    def _get_total_duration(self):
        self.total_duration=datetime.datetime.today()

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        with_ = ("WITH %s" % with_clause) if with_clause else ""

        select_ = """
            SELECT check_in,check_out 
        """

        for field in fields.values():
            select_ += field

        from_ = """
                visit_detail
        """ % from_clause

        groupby_ = """
            check_in
        """ % (groupby)

        return '%s (SELECT %s FROM %s GROUP BY %s)' % (with_, select_, from_, groupby_)

    # def init(self):
    #     # self._table = sale_report
    #     tools.drop_view_if_exists(self.env.cr, self._table)
    #     self.env.cr.execute("""CREATE or REPLACE VIEW %s as (%s)""" % (self._table, self._query()))
