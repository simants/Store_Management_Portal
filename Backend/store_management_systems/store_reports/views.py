from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView

from store_management_systems.services.views_services import ViewsServices


class ROIReport(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        kwargs.update({
            'request': self.request
        })
        service = 'roi_report'
        service_obj = ViewsServices(service_name=service)
        status_code, data = service_obj.execute_service(*args, **kwargs)
        return JsonResponse(data, safe=False, status=status_code)


class LossReport(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        kwargs.update({
            'request': self.request
        })
        service = 'loss_report'
        service_obj = ViewsServices(service_name=service)
        status_code, data = service_obj.execute_service(*args, **kwargs)
        return JsonResponse(data, safe=False, status=status_code)


class SalesReport(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        kwargs.update({
            'request': self.request
        })
        service = 'sales_report'
        service_obj = ViewsServices(service_name=service)
        status_code, data = service_obj.execute_service(*args, **kwargs)
        return JsonResponse(data, safe=False, status=status_code)


class EmployeePerformanceAnalysis(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        kwargs.update({
            'request': self.request
        })
        service = 'employee_performance_analysis'
        service_obj = ViewsServices(service_name=service)
        status_code, data = service_obj.execute_service(*args, **kwargs)
        return JsonResponse(data, safe=False, status=status_code)


class BusyHourAnalysis(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        kwargs.update({
            'request': self.request
        })
        service = 'busy_hour_analysis'
        service_obj = ViewsServices(service_name=service)
        status_code, data = service_obj.execute_service(*args, **kwargs)
        return JsonResponse(data, safe=False, status=status_code)


class BrandLocalPerformance(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        kwargs.update({
            'request': self.request
        })
        service = 'brand_local_performance'
        service_obj = ViewsServices(service_name=service)
        status_code, data = service_obj.execute_service(*args, **kwargs)
        return JsonResponse(data, safe=False, status=status_code)


class ExpenseReport(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        kwargs.update({
            'request': self.request
        })
        service = 'expense_report'
        service_obj = ViewsServices(service_name=service)
        status_code, data = service_obj.execute_service(*args, **kwargs)
        return JsonResponse(data, safe=False, status=status_code)


class PaymentTypeReport(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        kwargs.update({
            'request': self.request
        })
        service = 'payment_type_report'
        service_obj = ViewsServices(service_name=service)
        status_code, data = service_obj.execute_service(*args, **kwargs)
        return JsonResponse(data, safe=False, status=status_code)


class InventoryOptimization(APIView):
    def get(self, request, *args, **kwargs):
        kwargs.update({
            'request': request
        })
        service = 'inventory_optimization'
        service_obj = ViewsServices(service_name=service)
        status_code, data = service_obj.execute_service(*args, **kwargs)
        return JsonResponse(data, safe=False, status=status_code)


class CustomerAnalysis(APIView):
    def get(self, request, *args, **kwargs):
        kwargs.update({
            'request': request
        })
        service = 'customer_analysis'
        service_obj = ViewsServices(service_name=service)
        status_code, data = service_obj.execute_service(*args, **kwargs)
        return JsonResponse(data, safe=False, status=status_code)


class Stores(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        kwargs.update({
            'request': self.request
        })

        service = 'stores'
        service_obj = ViewsServices(service_name=service)
        status_code, data = service_obj.execute_service(*args, **kwargs)
        return JsonResponse(data, safe=False, status=status_code)


class DashboardValues(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        kwargs.update({
            'request': self.request
        })
        service = 'dashboard_values'
        service_obj = ViewsServices(service_name=service)
        status_code, data = service_obj.execute_service(*args, **kwargs)
        return JsonResponse(data, safe=False, status=status_code)


class DashboardSales(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        kwargs.update({
            'request': self.request
        })
        service = 'dashboard_sales'
        service_obj = ViewsServices(service_name=service)
        status_code, data = service_obj.execute_service(*args, **kwargs)
        return JsonResponse(data, safe=False, status=status_code)


class DashboardExpense(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        kwargs.update({
            'request': self.request
        })
        service = 'dashboard_expense'
        service_obj = ViewsServices(service_name=service)
        status_code, data = service_obj.execute_service(*args, **kwargs)
        return JsonResponse(data, safe=False, status=status_code)


class Products(APIView):
    def get(self, request, *args, **kwargs):
        kwargs.update({
            'request': self.request
        })
        service = 'get_products'
        service_obj = ViewsServices(service_name=service)
        status_code, data = service_obj.execute_service(*args, **kwargs)
        return JsonResponse(data, safe=False, status=status_code)

    def put(self, request, *args, **kwargs):
        kwargs.update({
            'request': self.request
        })
        service = 'put_products'
        service_obj = ViewsServices(service_name=service)
        status_code, data = service_obj.execute_service(*args,**kwargs)
        return JsonResponse(data, safe=False, status=status_code)

    def post(self, request, *args, **kwargs):
        kwargs.update({
            'request': self.request
        })
        service = 'post_products'
        service_obj = ViewsServices(service_name=service)
        status_code, data = service_obj.execute_service(*args,**kwargs)
        return JsonResponse(data, safe=False, status=status_code)
