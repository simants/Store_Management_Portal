from django.urls import path

from . import views

urlpatterns = [
    path('roi_report', views.ROIReport.as_view()),
    path('loss_report', views.LossReport.as_view()),
    path('sales_report', views.SalesReport.as_view()),
    path('expense_report', views.ExpenseReport.as_view()),
    path('payment_type_report', views.PaymentTypeReport.as_view()),
    path('brand_local_performance', views.BrandLocalPerformance.as_view()),
    path('dashboard_values', views.DashboardValues.as_view()),
    path('employee_performance_analysis', views.EmployeePerformanceAnalysis.as_view()),
    path('stores', views.Stores.as_view()),
    path('dashboard_sales', views.DashboardSales.as_view()),
    path('dashboard_expense', views.DashboardExpense.as_view()),
    path('products', views.Products.as_view()),
    path('products', views.Products.as_view()),
    path('busy_hour_analysis', views.BusyHourAnalysis.as_view())
]
