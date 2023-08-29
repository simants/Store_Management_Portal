import calendar
from datetime import datetime

from store_management_systems.commons.generic_constants import GenericConstants
from store_reports.services.service_helper.generic_service_helper import GenericServiceHelper


class BusyHourAnalysis(GenericServiceHelper):
    def __init__(self):
        super().__init__()
        self.sales_hours_query = """
            SELECT
                st.NAME,
                to_char(s.CREATED_AT, 'HH24:MM'),
                COUNT(s.ID)
            FROM 
                S22_S003_11_SALES s
            INNER JOIN
                S22_S003_11_STORE st
            ON
                st.ID = s.STORE_ID
            WHERE 1 = 1
            {where_clause}
            GROUP BY
                st.NAME,
                to_char(s.CREATED_AT, 'HH24:MM')
            ORDER BY
                st.NAME
        """

    def get_data(self, *args, **kwargs):
        params = self.get_request_params(*args, **kwargs)
        error_msg = self.check_errors(params)
        if self.status_code:
            return error_msg
        busy_hour_analysis = self.get_busy_hour_analysis(params)
        days = self.get_days(params['start_date'], params['end_date'], params['date_type'])
        for store in list(busy_hour_analysis.keys()):
            for key in list(busy_hour_analysis[store].keys()):
                busy_hour_analysis[store][key] = round(busy_hour_analysis[store][key] / days, 2)
        return busy_hour_analysis

    def get_busy_hour_analysis(self, query_filters):
        where_clause = self.get_where_clause(query_filters)
        sales_query = self.sales_hours_query.format(where_clause=where_clause)
        self.cur.execute(sales_query)
        rows = self.cur.fetchall()
        busy_hour_analysis = {}
        for data in rows:
            store_id = data[0]
            now = datetime.now().replace(hour=int(data[1].split(':')[0]), minute=int(data[1].split(':')[1]), second=0,
                                         microsecond=0)
            sales_count = data[2]
            if store_id not in busy_hour_analysis:
                busy_hour_analysis[store_id] = {
                    '6-12': 0,
                    '12-18': 0,
                    '18-24': 0
                }
            if datetime.now().replace(hour=6, minute=0, second=0, microsecond=0) <= now <= \
                    datetime.now().replace(hour=12, minute=0, second=0, microsecond=0):
                busy_hour_analysis[store_id]['6-12'] += sales_count
            elif datetime.now().replace(hour=12, minute=0, second=0, microsecond=0) < now <= \
                    datetime.now().replace(hour=18, minute=0, second=0, microsecond=0):
                busy_hour_analysis[store_id]['12-18'] += sales_count
            elif datetime.now().replace(hour=18, minute=0, second=0, microsecond=0) < now <= \
                    datetime.now().replace(hour=23, minute=59, second=59, microsecond=0):
                busy_hour_analysis[store_id]['12-18'] += sales_count
        return busy_hour_analysis

    def get_where_clause(self, query_filters):
        clause = ''
        clause = self.get_store_filter(query_filters['store_id'], clause, ['s'])
        clause = self.get_start_date_end_date_filter(query_filters['start_date'], query_filters['end_date'],
                                                     query_filters['date_type'], clause, ['s'])
        return clause

    def get_days(self, start_date, end_date, date_type):
        if date_type.lower() == GenericConstants.YEAR:
            start_date = datetime.strptime(start_date, '%Y')
            end_date = datetime.strptime(end_date, '%Y').replace(month=12, day=31, hour=23, minute=59, second=59)
        else:
            _ = end_date.split('-')
            start_date = datetime.strptime(start_date, '%Y-%m')
            end_date = datetime.strptime(end_date, '%Y-%m').replace(
                day=calendar.monthrange(_[1], _[0])[1], hour=23, minute=59, second=59)
        return (end_date.date() - start_date.date()).days
