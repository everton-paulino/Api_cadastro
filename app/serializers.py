from app.models import dados
from rest_framework import serializers

class dadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = dados
        fields = ['id', 'name', 'cpf', 'created_at', 'Active']