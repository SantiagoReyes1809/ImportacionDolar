import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions

# Create your views here.
class conversionDolares(APIView):
    def get(self,request,*args,**kwargs):

        valorDolar=3800
        pesosCol = float(request.GET.get('pesos'))
        conversion_moneda= float(pesosCol)/valorDolar

        conversion_moneda = f'Su valor digitado de {pesosCol} pesos equivale a {conversion_moneda} dolares'    
        return Response(conversion_moneda,status=status.HTTP_200_OK)