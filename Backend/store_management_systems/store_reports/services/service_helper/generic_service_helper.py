import calendar
from abc import ABC
from datetime import datetime, date, timedelta

from rest_framework import status

from store_management_systems.commons.generic_constants import GenericConstants
from store_management_systems.services.base_service import BaseService


class GenericServiceHelper(BaseService, ABC):

    def get_request_params(self, *args, **kwargs):
        date_type = kwargs['request'].query_params.get('year_or_month')
        start_date = kwargs['request'].query_params.get('start_date')
        end_date = kwargs['request'].query_params.get('end_date')
        store_id = kwargs['request'].query_params.get('store_id')

        return {
            'date_type': date_type,
            'start_date': start_date,
            'end_date': end_date,
            'store_id': store_id,
        }

    def set_status_code(self, *args, **kwargs):
        self.status_code = kwargs['status_code']

    @staticmethod
    def get_store_filter(store_id, clause, table_aliases):
        if store_id.lower() != GenericConstants.ALL:
            clause += "AND {0}.STORE_ID IN ({1})\n".format(table_aliases[0], store_id)
        return clause

    @staticmethod
    def get_feedback_store_filter(store_id, clause):
        if store_id.lower() != GenericConstants.ALL:
            clause += "AND STOREID_EMPID_SALEID IN ({0})".format(store_id)
        return clause

    @staticmethod
    def get_start_date_end_date_filter(start_date, end_date, date_type, clause, table_aliases):
        if start_date and end_date:
            if date_type.lower() == GenericConstants.YEAR:
                start_date = datetime.strftime(
                    datetime.strptime(start_date, '%Y'), '%Y-%m-%d %H:%M:%S'
                )
                end_date = datetime.strftime(
                    datetime.strptime(end_date, '%Y').replace(month=12, day=31, hour=23, minute=59, second=59),
                    '%Y-%m-%d %H:%M:%S'
                )
            else:
                _ = end_date.split('-')
                start_date = datetime.strftime(datetime.strptime(start_date, '%Y-%m'), '%Y-%m-%d %H:%M:%S')
                end_date = datetime.strftime(
                    datetime.strptime(end_date, '%Y-%m').replace(
                        day=calendar.monthrange(int(_[0]), int(_[1]))[1], hour=23, minute=59, second=59
                    ), '%Y-%m-%d %H:%M:%S'
                )
            clause += f"AND {table_aliases[0]}.created_at BETWEEN '{start_date}' AND '{end_date}'\n"
        return clause

    @staticmethod
    def get_days_filter(days, clause, table_aliases):
        today = date.today()
        if int(days) > 0:
            today = datetime.combine(today, datetime.min.time()) - timedelta(days=int(days))
        elif int(days) == 0:
            today = datetime.combine(today, datetime.min.time()).replace(day=1)
        clause += f" AND {table_aliases[0]}.created_at >= '{today}'"
        return clause

    def check_mandatory_param(self, param):
        if not param:
            self.set_status_code(status_code=status.HTTP_400_BAD_REQUEST)
            return True
        return False

    def check_start_date_end_date(self, start_date, end_date, year_or_month):
        if year_or_month == GenericConstants.YEAR:
            start_date = datetime.strptime(start_date, '%Y')
            end_date = datetime.strptime(end_date, '%Y').replace(month=12, day=31, hour=23, minute=59, second=59)

        elif year_or_month == GenericConstants.MONTH:
            _ = end_date.split('-')
            start_date = datetime.strftime(datetime.strptime(start_date, '%Y-%m'), '%Y-%m-%d %H:%M:%S')
            end_date = datetime.strftime(
                datetime.strptime(end_date, '%Y-%m').replace(
                    day=calendar.monthrange(int(_[0]), int(_[1]))[1], hour=23, minute=59, second=59
                ), '%Y-%m-%d %H:%M:%S'
            )

        if start_date > end_date:
            self.set_status_code(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
            return True
        return False

    def check_errors(self, params):
        if self.check_mandatory_param(params['store_id']):
            GenericConstants.MANDATORY_MESSAGE['message'] = GenericConstants.MANDATORY_MESSAGE['message'].\
                format('store_id')
            return GenericConstants.MANDATORY_MESSAGE

        if self.check_mandatory_param(params['date_type']):
            GenericConstants.MANDATORY_MESSAGE['message'] = GenericConstants.MANDATORY_MESSAGE['message']. \
                format('year_or_month')
            return GenericConstants.MANDATORY_MESSAGE

        if self.check_mandatory_param(params['start_date']):
            GenericConstants.MANDATORY_MESSAGE['message'] = GenericConstants.MANDATORY_MESSAGE['message']. \
                format('start_date')
            return GenericConstants.MANDATORY_MESSAGE

        if self.check_mandatory_param(params['end_date']):
            GenericConstants.MANDATORY_MESSAGE['message'] = GenericConstants.MANDATORY_MESSAGE['message']. \
                format('end_date')
            return GenericConstants.MANDATORY_MESSAGE

        if self.check_start_date_end_date(params['start_date'], params['end_date'], params['date_type']):
            return GenericConstants.INVALID_PARAMETERS
