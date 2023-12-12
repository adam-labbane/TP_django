from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ConcessionnairePostSerializer, ConcessionnaireSerializer, VoitureSerializer
from .models import Concessionnaire, Voiture


class ConcessionnaireViewSet(viewsets.ModelViewSet):
    queryset = Concessionnaire.objects.all()
    serializer_class = ConcessionnaireSerializer
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ConcessionnaireSerializer
        return ConcessionnairePostSerializer

class VoitureViewSet(viewsets.ModelViewSet):
    queryset = Voiture.objects.all()
    serializer_class = VoitureSerializer
