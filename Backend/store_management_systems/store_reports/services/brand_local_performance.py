from store_reports.services.service_helper.generic_service_helper import GenericServiceHelper


class BrandLocalPerformance(GenericServiceHelper):
    def __init__(self):
        super().__init__()
        self.brand_performance_query = """
            SELECT
                st.NAME,
                p.LOCAL_BRAND,
                SUM(od.QUANTITY_BOUGHT)
            FROM
                S22_S003_11_ORDER_DETAILS od
            INNER JOIN
                S22_S003_11_SALES s
            ON 
                s.ID = od.SALES_ID
            INNER JOIN
                S22_S003_11_PRODUCT p
            ON
                p.ID = od.PRODUCT_ID
            INNER JOIN
                S22_S003_11_STORE st
            ON
                st.ID = s.STORE_ID
            WHERE 1 = 1 {where_clause}
            GROUP BY
                st.NAME,
                p.local_brand
            ORDER BY
                st.NAME asc
        """

    def get_data(self, *args, **kwargs):
        params = self.get_request_params(*args, **kwargs)
        self.check_errors(params)
        return self.get_brand_performance_data(params)

    def get_brand_performance_data(self, params):
        where_clause = self.get_where_clause(['s'], params)
        brand_performance_query = self.brand_performance_query.format(where_clause=where_clause)
        self.cur.execute(brand_performance_query)
        rows = self.cur.fetchall()
        brand_local_performance_data = {
            'Store': list(),
            'Local': list(),
            'Brand': list()
        }
        for row in rows:
            if row[0] not in brand_local_performance_data['Store']:
                brand_local_performance_data['Store'].append(row[0])
            if row[1] == 'l':
                brand_local_performance_data['Local'].append(row[2])
            elif row[1] == 'b':
                brand_local_performance_data['Brand'].append(row[2])
        return brand_local_performance_data

    def get_where_clause(self, table_aliases, query_filters):
        clause = ''
        clause = self.get_store_filter(query_filters['store_id'], clause, table_aliases)
        clause = self.get_start_date_end_date_filter(query_filters['start_date'], query_filters['end_date'],
                                                     query_filters['date_type'], clause, table_aliases)
        return clause
