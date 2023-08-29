from store_management_systems.commons.generic_constants import GenericConstants
from store_reports.services.service_helper.generic_service_helper import GenericServiceHelper


class DashboardSales(GenericServiceHelper):

    def __init__(self):
        super().__init__()
        self.sales_query = """
            SELECT
                s.created_at,
                SUM(s.TOTAL)
            FROM
                S22_S003_11_SALES s
            WHERE 1 = 1
            {where_clause}
            GROUP BY
                s.created_at
        """

    def get_request_params(self, *args, **kwargs):
        store_id = kwargs['request'].query_params.get('store_id')
        days = kwargs['request'].query_params.get('days')

        return {
            'store_id': store_id,
            'days': days
        }

    def get_data(self, *args, **kwargs):
        params = self.get_request_params(*args, **kwargs)
        error_message = self.error_checks(params)
        if self.status_code:
            return error_message
        return self.get_dashboard_sales(params)

    def error_checks(self, params):
        if self.check_mandatory_param(params['store_id']):
            GenericConstants.MANDATORY_MESSAGE['message'] = GenericConstants.MANDATORY_MESSAGE['message'].format(
                'store_id')
            return GenericConstants.MANDATORY_MESSAGE

        if self.check_mandatory_param(params['days']):
            GenericConstants.MANDATORY_MESSAGE['message'] = GenericConstants.MANDATORY_MESSAGE['message'].format('days')
            return GenericConstants.MANDATORY_MESSAGE

    def get_dashboard_sales(self, query_filters):
        where_clause = self.get_where_clause(query_filters)
        query = self.sales_query.format(where_clause=where_clause)
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return self.get_dashboard_sales_response(rows)

    def get_where_clause(self, query_filters):
        clause = ''
        clause = self.get_store_filter(query_filters['store_id'], clause, 's')
        clause = self.get_days_filter(query_filters['days'], clause, 's')
        return clause

    @staticmethod
    def get_dashboard_sales_response(query_rows):
        sales_response = {}
        for data in query_rows:
            _date = data[0]
            day = _date.strftime('%A')
            if day not in sales_response:
                sales_response[day] = 0
            sales_response[day] = round(sales_response[day] + data[1], 4)
        return sales_response
