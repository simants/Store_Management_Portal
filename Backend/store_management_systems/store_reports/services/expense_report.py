import calendar
from datetime import datetime

from store_management_systems.commons.generic_constants import GenericConstants
from store_reports.services.service_helper.generic_service_helper import GenericServiceHelper


class ExpenseReport(GenericServiceHelper):

    def __init__(self):
        super().__init__()
        self.expense_query = """
            SELECT 
                ec.NAME, 
                e.STORE_ID, 
                SUM(e.amount) TOTAL_EXPENSE_COST
            FROM 
                S22_S003_11_EXPENSE e
            INNER JOIN 
                S22_S003_11_EXPENSE_CATEGORY ec
            ON 
                e.CATEGORY_ID = ec.ID
            WHERE 
                1 = 1 
                {where_clause}
            GROUP BY 
                ec.NAME, 
                e.STORE_ID
        """

    def get_data(self, *args, **kwargs):
        params = self.get_request_params(*args, **kwargs)
        error_msg = self.check_errors(params)
        if self.status_code:
            return error_msg
        return self.get_expense_data(params)

    def get_expense_data(self, params):
        where_clause = self.get_where_clause(['e'], params)
        lost_data_query = self.expense_query.format(where_clause=where_clause)
        self.cur.execute(lost_data_query)
        rows = self.cur.fetchall()
        expense_report_data = {}
        for row in rows:
            product_category = row[0]
            store_id = row[1]
            expense = float("{:.2f}".format(row[2]))
            if store_id not in expense_report_data:
                expense_report_data[store_id] = dict()
                expense_report_data[store_id]['category_details'] = list()
                expense_report_data[store_id]['total_expense'] = 0
            expense_report_data[store_id]['category_details'].append({
                'expense_category': product_category,
                'expense': expense
            })
            expense_report_data[store_id]['total_expense'] = \
                float("{:2f}".format(expense_report_data[store_id]['total_expense'] + expense))
        return expense_report_data

    def get_where_clause(self, table_aliases, query_filters):
        clause = ''
        clause = self.get_store_filter(query_filters['store_id'], clause, table_aliases)
        clause = self.get_start_date_end_date_filter(query_filters['start_date'], query_filters['end_date'],
                                                     query_filters['date_type'], clause, table_aliases)
        return clause
