from store_reports.services.service_helper.generic_service_helper import GenericServiceHelper


class Stores(GenericServiceHelper):
    def __init__(self):
        super().__init__()
        self.store_query = """
            SELECT
                ID,
                NAME
            FROM
                S22_S003_11_STORE
        """

    def get_request_params(self, *args, **kwargs):
        pass

    def get_data(self, *args, **kwargs):
        self.cur.execute(self.store_query)
        rows = self.cur.fetchall()
        store_details = {}
        for row in rows:
            store_details[row[0]] = row[1]

        return store_details
