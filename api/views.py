from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ConcessionnaireSerializer
from .models import Concessionnaire


class ConcessionnaireSerializer(viewsets.ModelViewSet):
    queryset = Concessionnaire.objects.all()
    serializer_class = ConcessionnaireSerializer
