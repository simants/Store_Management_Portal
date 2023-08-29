from store_management_systems.commons.generic_constants import GenericConstants
from store_reports.services.service_helper.generic_service_helper import GenericServiceHelper


class DashboardValues(GenericServiceHelper):
    def __init__(self):
        super().__init__()
        self.revenue_query = """
            SELECT 
                SUM(s.total) REVENUE
            FROM 
                S22_S003_11_SALES s
            WHERE
                1=1 
                {where_clause}
            """
        self.expense_query = """
            SELECT 
                SUM(e.amount) EXPENSE 
            FROM 
                S22_S003_11_EXPENSE e
            WHERE 
                1=1
                {where_clause}
            """

        self.rating_query = """
            SELECT 
                AVG(f.rating)
            FROM 
                S22_S003_11_FEEDBACK f
            WHERE 
                1=1
                {where_clause}
            """

    def get_request_params(self, *args, **kwargs):
        store_id = kwargs['request'].query_params.get('store_id')
        return {
            'store_id': store_id
        }

    def get_data(self, *args, **kwargs):
        params = self.get_request_params(*args, **kwargs)
        error_msg = self.error_checks(params)
        if self.status_code:
            return error_msg

        return self.get_dashboard_values(params)

    def error_checks(self, params):
        if self.check_mandatory_param(params['store_id']):
            GenericConstants.MANDATORY_MESSAGE['message'] = GenericConstants.MANDATORY_MESSAGE['message'].\
                format('store_id')
            return GenericConstants.MANDATORY_MESSAGE

    def get_dashboard_values(self, query_filters):
        where_clause = self.get_where_clause(['s'], query_filters)
        revenue_query = self.revenue_query.format(where_clause=where_clause)
        where_clause = self.get_where_clause(['e'], query_filters)
        expense_query = self.expense_query.format(where_clause=where_clause)
        where_clause = self.get_where_clause(['f'], query_filters, feedback=True)
        rating_query = self.rating_query.format(where_clause=where_clause)
        self.cur.execute(revenue_query)
        rows_rev = self.cur.fetchall()[0][0]
        self.cur.execute(expense_query)
        rows_exp = self.cur.fetchall()[0][0]
        self.cur.execute(rating_query)
        rows_rat = self.cur.fetchall()[0][0]
        return {
            'revenue': round(rows_rev, 2),
            'expense': round(rows_exp, 2),
            'profit_loss': round(rows_rev - rows_exp, 2),
            'rating': round(rows_rat, 2)
        }

    def get_where_clause(self, table_aliases, query_filters, feedback=False):
        clause = ''
        if feedback:
            return self.get_feedback_store_filter(query_filters['store_id'], clause)
        return self.get_store_filter(query_filters['store_id'], clause, table_aliases)
