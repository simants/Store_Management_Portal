from store_management_systems.commons.generic_constants import GenericConstants
from store_reports.services.service_helper.generic_service_helper import GenericServiceHelper


class DashboardExpense(GenericServiceHelper):
    def __init__(self):
        super().__init__()
        self.expense_query = """
            SELECT
                ec.name,
                SUM(amount)
            FROM
                S22_S003_11_EXPENSE e
            INNER JOIN
                S22_S003_11_EXPENSE_CATEGORY ec
            ON 
                e.CATEGORY_ID = ec.ID
            WHERE 1 = 1
            {where_clause}
            GROUP BY
                ec.name
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
        return self.get_dashboard_expenses(params)

    def error_checks(self, params):
        if self.check_mandatory_param(params['store_id']):
            GenericConstants.MANDATORY_MESSAGE['message'] = GenericConstants.MANDATORY_MESSAGE['message'].\
                format('store_id')
            return GenericConstants.MANDATORY_MESSAGE

    def get_dashboard_expenses(self, query_filters):
        where_clause = self.get_where_clause(query_filters)
        query = self.expense_query.format(where_clause=where_clause)
        self.cur.execute(query)
        rows = self.cur.fetchall()
        dashboard_expense = {}
        for data in rows:
            dashboard_expense[data[0]] = data[1]
        return dashboard_expense


    def get_where_clause(self, query_filters):
        clause = ''
        return self.get_store_filter(query_filters['store_id'], clause, ['e'])
