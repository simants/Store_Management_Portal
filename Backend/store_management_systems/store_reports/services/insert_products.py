import traceback

from store_management_systems.commons.generic_constants import GenericConstants
from store_reports.services.service_helper.generic_service_helper import GenericServiceHelper


class InsertProducts(GenericServiceHelper):
    def __init__(self):
        super().__init__()
        self.product_query = """
            SELECT MAX(barcode) FROM S22_S003_11_PRODUCT
        """
        self.product_insert_query = """
            INSERT INTO 
            S22_S003_11_PRODUCT 
            (name, category_id, cost_price, selling_price, inventory, barcode, local_brand, store_id, created_at, updated_at)
            values ('{product_name}', {category_id}, {cost_price}, {selling_price}, {inventory}, '{barcode}', 
            '{local_brand}', {store_id}, SYSDATE, SYSDATE)
        """

    def get_request_params(self, *args, **kwargs):
        store_id = kwargs['request'].data['store_id']
        category_id = kwargs['request'].data['product_category_id']
        product_name = kwargs['request'].data['product_name']
        cost_price = kwargs['request'].data['cost_price']
        selling_price = kwargs['request'].data['selling_price']
        inventory = kwargs['request'].data['inventory']
        local_brand = kwargs['request'].data['local_brand']
        return {
            'store_id': store_id,
            'category_id': category_id,
            'product_name': product_name,
            'cost_price': cost_price,
            'selling_price': selling_price,
            'inventory': inventory,
            'local_brand': local_brand
        }

    def get_data(self, *args, **kwargs):
        params = self.get_request_params(*args, **kwargs)
        error_msg = self.error_checks(params)
        if self.status_code:
            return error_msg
        params['barcode'] = self.get_barcode()
        return self.insert_products(params)

    def error_checks(self, params):
        if self.check_mandatory_param(params['store_id']):
            GenericConstants.MANDATORY_MESSAGE['message'] = GenericConstants.MANDATORY_MESSAGE['message']. \
                format('store_id')
            return GenericConstants.MANDATORY_MESSAGE
        if self.check_mandatory_param(params['category_id']):
            GenericConstants.MANDATORY_MESSAGE['message'] = GenericConstants.MANDATORY_MESSAGE['message']. \
                format('category_id')
            return GenericConstants.MANDATORY_MESSAGE
        if self.check_mandatory_param(params['product_name']):
            GenericConstants.MANDATORY_MESSAGE['message'] = GenericConstants.MANDATORY_MESSAGE['message']. \
                format('product_name')
            return GenericConstants.MANDATORY_MESSAGE
        if self.check_mandatory_param(params['cost_price']):
            GenericConstants.MANDATORY_MESSAGE['message'] = GenericConstants.MANDATORY_MESSAGE['message']. \
                format('cost_price')
            return GenericConstants.MANDATORY_MESSAGE
        if self.check_mandatory_param(params['selling_price']):
            GenericConstants.MANDATORY_MESSAGE['message'] = GenericConstants.MANDATORY_MESSAGE['message']. \
                format('selling_price')
            return GenericConstants.MANDATORY_MESSAGE
        if self.check_mandatory_param(params['inventory']):
            GenericConstants.MANDATORY_MESSAGE['message'] = GenericConstants.MANDATORY_MESSAGE['message']. \
                format('inventory')
            return GenericConstants.MANDATORY_MESSAGE
        if self.check_mandatory_param(params['local_brand']):
            GenericConstants.MANDATORY_MESSAGE['message'] = GenericConstants.MANDATORY_MESSAGE['message']. \
                format('local_brand')
            return GenericConstants.MANDATORY_MESSAGE

    def get_barcode(self):
        self.cur.execute(self.product_query)
        return self.cur.fetchall()[0][0]

    def insert_products(self, params):
        try:
            insert_query = self.product_insert_query.format(
                product_name=params['product_name'], category_id=params['category_id'], cost_price=params['cost_price'],
                selling_price=params['selling_price'], inventory=params['inventory'], barcode=params['barcode'],
                local_brand=params['local_brand'], store_id=params['store_id']
            )
            print(insert_query)
            self.cur.execute(insert_query)
            self.cur.execute('COMMIT')
            return GenericConstants.INSERT_SUCCESS_MESSAGE

        except Exception:
            traceback.print_exc()
            return GenericConstants.INSERT_ERROR_MESSAGE
