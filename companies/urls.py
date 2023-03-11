# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.CompanyList.as_view(), name='list_companies'),
    url(r'^stats/$', views.company_stats_api_view, name='company_stats_api_view'),
    path('<id>/', views.CompanyRetrieve.as_view(), name='get_company'),
    url(r'^stats/view/$', views.company_stats_view, name='company_stats_view')
]
