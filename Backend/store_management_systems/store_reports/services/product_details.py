from store_management_systems.commons.generic_constants import GenericConstants
from store_reports.services.service_helper.generic_service_helper import GenericServiceHelper


class ProductDetails(GenericServiceHelper):
    def __init__(self):
        super().__init__()
        # self.page = '1'
        # self.limit = '10'
        # self.order_by = 's.NAME'
        # self.sort_order = 'asc'
        self.product_query = """
            SELECT 
                s.NAME,
                p.STORE_ID,
                pc.NAME,
                p.CATEGORY_ID,
                p.NAME,
                p.ID,
                p.COST_PRICE,
                p.SELLING_PRICE,
                p.INVENTORY
            FROM 
                S22_S003_11_PRODUCT p
            INNER JOIN
                S22_S003_11_PRODUCT_CATEGORY pc
            ON
                p.CATEGORY_ID = pc.ID
            INNER JOIN
                S22_S003_11_STORE s
            ON s.ID = p.STORE_ID
            WHERE p.STATUS = 1
            {where_clause}
        """

    def get_request_params(self, *args, **kwargs):
        store_id = kwargs['request'].query_params.get('store_id')
        search = kwargs['request'].query_params.get('search')
        # page = kwargs['request'].query_params.get('page')
        # if page:
        #     self.page = page
        #
        # limit = kwargs['request'].query_params.get('limit')
        # if limit:
        #     self.limit = limit

        # order_by = kwargs['request'].query_params.get('order_by')
        # if order_by:
        #     self.order_by = order_by
        #
        # sort_order = kwargs['request'].query_params.get('sort_order')
        # if sort_order:
        #     self.sort_order = sort_order
        return {
            'store_id': store_id,
            'search': search,
            # 'page': self.page,
            # 'limit': self.limit,
            # 'order_by': self.order_by,
            # 'sort_order': self.sort_order
        }

    def get_data(self, *args, **kwargs):
        params = self.get_request_params(*args, **kwargs)
        error_msg = self.error_checks(params)
        if self.status_code:
            return error_msg
        return self.get_product_details(params)

    def error_checks(self, params):
        if self.check_mandatory_param(params['store_id']):
            GenericConstants.MANDATORY_MESSAGE['message'] = GenericConstants.MANDATORY_MESSAGE['message'].\
                format('store_id')
            return GenericConstants.MANDATORY_MESSAGE

    def get_product_details(self, query_filters):
        where_clause = self.get_where_clause(query_filters)
        product_query = self.product_query.format(
            where_clause=where_clause
        )
        print(product_query)
        self.cur.execute(product_query)
        rows = self.cur.fetchall()
        self.cur.execute('COMMIT')
        print(len(rows))
        return self.get_product_details_response(query_filters, rows)

    def get_where_clause(self, query_filters):
        clause = ''
        clause = self.get_store_filter(query_filters['store_id'], clause, ['p'])
        clause = self.get_search_filters(query_filters['search'], clause, ['p', 'pc'])
        return clause

    @staticmethod
    def get_search_filters(search, clause, table_aliases):
        if search != '0':
            clause = f"{clause} \n" \
                     f"AND (LOWER({table_aliases[0]}.NAME) LIKE '%{search.lower()}%'\n" \
                     f"OR LOWER({table_aliases[1]}.NAME) LIKE '%{search.lower()}%')"
        return clause

    @staticmethod
    def get_product_details_response(params, rows):
        # next_page = None
        # curr_page = int(params['page'])
        # total_count = len(rows)
        # limit = int(params['limit'])
        # offset = (curr_page - 1) * limit
        # if total_count > curr_page * limit:
        #     next_page = curr_page + 1
        data = []
        for d in rows:
            data.append({
                'store_name': d[0],
                'store_id': d[1],
                'product_category': d[2],
                'product_category_id': d[3],
                'product_name': d[4],
                'product_id': d[5],
                'cost_price': d[6],
                'selling_price': d[7],
                'inventory': d[8]
            })
        return {
            'data': data,
        }
