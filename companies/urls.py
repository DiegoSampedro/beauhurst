# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.CompanyList.as_view(), name='list_companies'),
    url(r'^stats/$', views.company_stats_api_view, name='company_stats_api_view'),
    path('<int:id>/', views.CompanyRetrieve.as_view(), name='get_company'),
    path('my-companies/', views.my_companies, name='my_companies'),
    url(r'^stats/view/$', views.company_stats_view, name='company_stats_view')
]
