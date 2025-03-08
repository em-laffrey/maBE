from rest_framework import serializers

from maBE.models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zip_code', 'country']
