from store_management_systems.commons.generic_constants import GenericConstants
from store_reports.services.service_helper.generic_service_helper import GenericServiceHelper


class PaymentTypeReport(GenericServiceHelper):
    def __init__(self):
        super().__init__()
        self.payment_type_query = """
            SELECT
                st.NAME,
                pd.MODE_OF_PAYMENT,
                COUNT(pd.SALES_ID)
            FROM
                S22_S003_11_PAYMENT_DETAILS pd
            INNER JOIN 
                S22_S003_11_SALES s
            ON
                s.ID = pd.SALES_ID
            INNER JOIN
                S22_S003_11_STORE st
            ON
                st.ID = s.STORE_ID
            WHERE 1 = 1 {where_clause}
            GROUP BY
                st.NAME,
                pd.MODE_OF_PAYMENT
            ORDER BY
                st.NAME
        """

    def get_data(self, *args, **kwargs):
        params = self.get_request_params(*args, **kwargs)
        error_msg = self.check_errors(params)
        if self.status_code:
            return error_msg
        return self.get_payment_type_data(params)

    def get_payment_type_data(self, params):
        where_clause = self.get_where_clause(params, ['s'])
        payment_type_data_query = self.payment_type_query.format(where_clause=where_clause)
        self.cur.execute(payment_type_data_query)
        rows = self.cur.fetchall()
        payment_type_report_data = {
            'Store': list(),
            'Cash': list(),
            'Card': list()
        }
        for row in rows:
            if row[0] not in payment_type_report_data['Store']:
                payment_type_report_data['Store'].append(row[0])
            if row[1] == 'CASH':
                payment_type_report_data['Cash'].append(row[2])
            elif row[1] == 'CARD':
                payment_type_report_data['Card'].append(row[2])
        return payment_type_report_data

    def get_where_clause(self, query_filters, table_aliases):
        clause = ''
        clause = self.get_store_filter(query_filters['store_id'], clause, table_aliases)
        clause = self.get_start_date_end_date_filter(query_filters['start_date'], query_filters['end_date'],
                                                     query_filters['date_type'], clause, table_aliases)
        return clause
