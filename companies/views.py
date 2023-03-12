# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Company
from .serializers import CompanySerializer


def most_recently_founded_companies(limit=10):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)

    if limit:
        companies = companies[:limit]

    return sorted(serializer.data, key=lambda comp: comp['date_founded'])


def company_stats_api_view(request):
    response = {
        'most_recently_founded': most_recently_founded_companies(),
        # NOTE: The below is dummy data so you can work on the front end without
        # building out the API first. Replace the dummy data below once you've
        # built functional replacements.
        'average_employee_count': 5.0,
        'companies_founded_per_quarter': [
            {'year': 2017, 'quarter': 1, 'value': 5},
            {'year': 2017, 'quarter': 2, 'value': 10},
            {'year': 2017, 'quarter': 3, 'value': 3},
            {'year': 2017, 'quarter': 4, 'value': 15},
            {'year': 2018, 'quarter': 1, 'value': 24},
        ],
        'user_created_most_companies': 'Jeff',
        'user_created_most_employees': 'Jane',
        'average_deal_amount_raised_by_country': [
            {'country': 'gb', 'average_deal_amount_raised': 500.0},
            {'country': 'fr', 'average_deal_amount_raised': 450.0},
        ]
    }
    return JsonResponse(response)


class CompanyList(generics.ListCreateAPIView):
   queryset = Company.objects.all()
   serializer_class = CompanySerializer

class CompanyRetrieve(generics.RetrieveAPIView):
   queryset = Company.objects.all()
   serializer_class = CompanySerializer
   lookup_field = 'id'


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_companies(request):
    user_id = request.user.id
    companies = Company.objects.filter(monitors=user_id)
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)


def company_stats_view(request):
    return render(request, 'companies/company_stats.html')
