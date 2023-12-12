from rest_framework import routers

from .views import ConcessionnaireViewSet, VoitureViewSet

api_router = routers.DefaultRouter()
api_router.register('concessionnaire', ConcessionnaireViewSet)
api_router.register('voiture', VoitureViewSet)