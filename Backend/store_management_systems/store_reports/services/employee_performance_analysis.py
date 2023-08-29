from store_management_systems.commons.generic_constants import GenericConstants
from store_reports.services.service_helper.generic_service_helper import GenericServiceHelper


class EmployeePerformanceAnalysis(GenericServiceHelper):
    def __init__(self):
        super().__init__()
        self.employee_performance_query = """
            SELECT 
                st.NAME, 
                e.name, 
                AVG(f.RATING)
            FROM
                S22_S003_11_FEEDBACK f
            INNER JOIN
                S22_S003_11_EMPLOYEE e
            ON
                f.STOREID_EMPID_SALEID = e.ID
            INNER JOIN
                S22_S003_11_STORE st
            ON
                st.ID = e.STORE_ID
            WHERE
                f.TYPEID = 2
                {where_clause}
            GROUP BY
                e.name,
                st.NAME
        """

    def get_data(self, *args, **kwargs):
        params = self.get_request_params(*args, **kwargs)
        error_message = self.check_errors(params)
        if self.status_code:
            return error_message
        return self.get_employee_performance_data(params)

    def get_employee_performance_data(self, params):
        where_clause = self.get_where_clause(params)
        query = self.employee_performance_query.format(where_clause=where_clause)
        self.cur.execute(query)
        rows = self.cur.fetchall()
        employee_performance = []
        for row in rows:
            # if row[0] not in employee_performance:
            #     employee_performance[row[0]] = list()
            employee_performance.append({
                'store': row[0],
                'employee_name': row[1],
                'average_rating': round(row[2], 2)
            })
        return employee_performance

    def get_where_clause(self, query_filters):
        clause = ''
        clause = self.get_store_filter(query_filters['store_id'], clause, ['e'])
        clause = self.get_start_date_end_date_filter(query_filters['start_date'], query_filters['end_date'],
                                                     query_filters['date_type'], clause, ['f'])
        return clause
