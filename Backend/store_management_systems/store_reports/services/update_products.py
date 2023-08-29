from store_management_systems.commons.generic_constants import GenericConstants
from store_reports.services.service_helper.generic_service_helper import GenericServiceHelper


class UpdateProducts(GenericServiceHelper):
    def __init__(self):
        super().__init__()
        self.update_products_query = """
        UPDATE 
            S22_S003_11_PRODUCT p
        SET 
            {set_statement}
        WHERE 1 = 1
            {where_clause}
        """
        self.table_col_map = {
            'category_id': 'category_id',
            'product_name': 'name',
            'cost_price': 'cost_price',
            'selling_price': 'selling_price',
            'inventory': 'inventory',
            'status': 'status'
        }

    def get_request_params(self, *args, **kwargs):
        product_id = kwargs['request'].data.get('product_id')
        category_id = kwargs['request'].data.get('product_category_id')
        product_name = kwargs['request'].data.get('product_name')
        cost_price = kwargs['request'].data.get('cost_price')
        selling_price = kwargs['request'].data.get('selling_price')
        inventory = kwargs['request'].data.get('inventory')
        status = kwargs['request'].data.get('status')
        return {
            'product_id': product_id,
            'category_id': category_id,
            'product_name': product_name,
            'cost_price': cost_price,
            'selling_price': selling_price,
            'inventory': inventory,
            'status': status
        }

    def get_data(self, *args, **kwargs):
        params = self.get_request_params(*args, **kwargs)
        error_msg = self.error_checks(params)
        if self.status_code:
            return error_msg
        return self.put_product_data(params)

    def error_checks(self, params):
        if self.check_mandatory_param(params['product_id']):
            GenericConstants.MANDATORY_MESSAGE['message'] = GenericConstants.MANDATORY_MESSAGE['message']. \
                format('product_id')
            return GenericConstants.MANDATORY_MESSAGE

    def put_product_data(self, params):
        where_clause = self.get_where_clause(params)
        set_clause = self.get_set_clause(params)
        update_products_query = self.update_products_query.format(where_clause=where_clause, set_statement=set_clause)
        try:
            print(update_products_query)
            self.cur.execute(update_products_query)
            self.cur.execute('COMMIT')
            return GenericConstants.UPDATE_SUCCESS_MSG
        except Exception:
            return GenericConstants.UPDATE_ERROR_MSG

    @staticmethod
    def get_where_clause(query_filters):
        return f" AND ID = {query_filters['product_id']}"

    def get_set_clause(self, query_filters):
        clause = []
        if query_filters['category_id']:
            clause.append(f"{self.table_col_map['category_id']} = {query_filters['category_id']}")

        if query_filters['product_name']:
            clause.append(f"{self.table_col_map['product_name']} = '{query_filters['product_name']}'")

        if query_filters['cost_price']:
            clause.append(f"{self.table_col_map['cost_price']} = {query_filters['cost_price']}")

        if query_filters['selling_price']:
            clause.append(f"{self.table_col_map['selling_price']} = {query_filters['selling_price']}")

        if query_filters['inventory']:
            clause.append(f"{self.table_col_map['inventory']} = {query_filters['inventory']}")

        if query_filters['status'] == 0 or query_filters['status'] == 1:
            clause.append(f"{self.table_col_map['status']} = {query_filters['status']}")
        return ', '.join(clause)
