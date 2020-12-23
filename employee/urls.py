from django.contrib import admin
from django.urls import path
from employee.views import *
from employee import views


urlpatterns = [

    path('company-details/<int:pk>/', views.CompanyDetailsApiView.as_view()),
    path('department-details/<int:pk>/', views.DepartmentDetailsApiView.as_view()),    
]