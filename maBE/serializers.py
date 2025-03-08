from rest_framework import serializers

from models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address', 'city', 'state', 'zip_code', 'country']
