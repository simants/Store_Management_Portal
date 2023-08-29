from store_management_systems.commons.generic_constants import GenericConstants
from store_reports.services.service_helper.generic_service_helper import GenericServiceHelper


class LossReport(GenericServiceHelper):
    def __init__(self):
        super().__init__()
        self.loss_query = """
            SELECT 
                pc.NAME, 
                st.NAME, 
                SUM(p.LOSS_DAMAGE) LOSS_DAMAGE_COUNT
            FROM 
                S22_S003_11_PRODUCT p
            INNER JOIN 
                S22_S003_11_PRODUCT_CATEGORY pc
            ON 
                p.CATEGORY_ID = pc.ID
            INNER JOIN
                S22_S003_11_STORE st
            ON
                st.ID = p.STORE_ID
            WHERE 
                1 = 1 
                {where_clause}
            GROUP BY 
                pc.NAME, 
                st.NAME
            ORDER BY
                st.NAME
        """

    def get_data(self, *args, **kwargs):
        params = self.get_request_params(*args, **kwargs)
        error_msg = self.check_errors(params)
        if self.status_code:
            return error_msg
        return self.get_loss_data(params)

    def get_loss_data(self, params):
        where_clause = self.get_where_clause(['p'], params)
        lost_data_query = self.loss_query.format(where_clause=where_clause)
        self.cur.execute(lost_data_query)
        rows = self.cur.fetchall()
        loss_report_data = {}
        for row in rows:
            product_category = row[0]
            store_id = row[1]
            loss_damage_quantity = row[2]
            if store_id not in loss_report_data:
                loss_report_data[store_id] = list()
            loss_report_data[store_id].append({
                'product_category': product_category,
                'loss_damage_quantity': loss_damage_quantity
            })
        return loss_report_data

    def get_where_clause(self, table_aliases, query_filters):
        clause = ''
        clause = self.get_store_filter(query_filters['store_id'], clause, table_aliases)
        clause = self.get_start_date_end_date_filter(query_filters['start_date'], query_filters['end_date'],
                                                     query_filters['date_type'], clause, table_aliases)
        return clause
