# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Company
from .serializers import CompanySerializer
from .service import CompanyStatsService


def company_stats_api_view(request):
    service = CompanyStatsService()
    response = service.get_company_stats()
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
