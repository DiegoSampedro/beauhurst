# -*- coding: utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
    path('', views.CompanyList.as_view(), name='list_companies'),
    path('stats/', views.company_stats_api_view, name='company_stats_api_view'),
    path('<int:id>/', views.CompanyRetrieve.as_view(), name='get_company'),
    path('my-companies/', views.my_companies, name='my_companies'),
    path('stats/view/', views.company_stats_view, name='company_stats_view')
]
