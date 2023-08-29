import calendar
from datetime import datetime

from rest_framework import status

from store_management_systems.commons.generic_constants import GenericConstants
from store_reports.services.service_helper.generic_service_helper import GenericServiceHelper


class SalesReport(GenericServiceHelper):
    def __init__(self):
        super().__init__()
        self.sales_query = """
            SELECT 
                pc.NAME, 
                s.STORE_ID, 
                SUM(s.TOTAL)
            FROM 
                S22_S003_11_SALES s
            INNER JOIN 
                S22_S003_11_ORDER_DETAILS od
            ON 
                s.ID = od.SALES_ID
            INNER JOIN 
                S22_S003_11_PRODUCT p
            ON
                p.ID = od.PRODUCT_ID
            INNER JOIN
                S22_S003_11_PRODUCT_CATEGORY pc
            ON
                pc.ID = p.CATEGORY_ID
            WHERE 
                1 = 1 
                {where_clause}
            GROUP BY 
                pc.NAME, 
                s.STORE_ID
        """

    def get_data(self, *args, **kwargs):
        params = self.get_request_params(*args, **kwargs)
        error_msg = self.check_errors(params)
        if self.status_code:
            return error_msg
        return self.get_sales_data(params)

    def get_sales_data(self, params):
        where_clause = self.get_where_clause(['s'], params)
        sales_data_query = self.sales_query.format(where_clause=where_clause)
        self.cur.execute(sales_data_query)
        rows = self.cur.fetchall()
        sales_report_data = {}
        for row in rows:
            product_category = row[0]
            store_id = row[1]
            sale = float("{:.2f}".format(row[2]))
            if store_id not in sales_report_data:
                sales_report_data[store_id] = dict()
                sales_report_data[store_id]['category_details'] = list()
                sales_report_data[store_id]['total_sales'] = 0
            sales_report_data[store_id]['category_details'].append({
                'product_category': product_category,
                'sale': sale
            })
            sales_report_data[store_id]['total_sales'] = \
                float("{:2f}".format(sales_report_data[store_id]['total_sales'] + sale))
        return sales_report_data

    def get_where_clause(self, table_aliases, query_filters):
        clause = ''
        clause = self.get_store_filter(query_filters['store_id'], clause, table_aliases)
        clause = self.get_start_date_end_date_filter(
            query_filters['start_date'], query_filters['end_date'], query_filters['date_type'], clause, table_aliases
        )
        return clause
