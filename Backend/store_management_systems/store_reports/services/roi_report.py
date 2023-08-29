from store_reports.services.service_helper.generic_service_helper import GenericServiceHelper


class ROIReport(GenericServiceHelper):
    def __init__(self):
        super().__init__()

    def get_request_params(self, *args, **kwargs):
        pass

    def get_data(self, *args, **kwargs):
        return {'Hi': 'Hi'}
