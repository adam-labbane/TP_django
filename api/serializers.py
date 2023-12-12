from rest_framework import serializers

from .models import Concessionnaire, Voiture


class ConcessionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concessionnaire
        fields = ('id', 'nom', 'code_postal')
class ConcessionnairePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concessionnaire
        fields = ('id', 'nom','numero_siret', 'code_postal')

class VoitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voiture
        fields = ('__all__')