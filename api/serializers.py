from rest_framework import serializers

from .models import Concessionnaire


class ConcessionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concessionnaire
        fields = ('id', 'nom', 'numero_siret', 'code_postal')