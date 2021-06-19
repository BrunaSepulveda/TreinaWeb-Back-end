from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .service.cidades_atendimento_service import listar_diaristas_cidade
from .serealizer import diaristas_cidade_serealizer
from .pagination import diaristas_cidade_pagination
# Create your views here.
class DiaristaCidadeList(APIView, diaristas_cidade_pagination.DiaristasCidadePagination):
    def get(self, request, format=None):
        cep = self.request.query_params.get('cep', None)
        diaristas = listar_diaristas_cidade(cep)
        resultado = self.paginate_queryset(diaristas, request)
        serealizer = diaristas_cidade_serealizer.DiaristaCidadeSerealizer(resultado, many=True, context={"request": request})

        return self.get_paginated_response(serealizer.data)