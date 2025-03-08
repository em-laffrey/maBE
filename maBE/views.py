from models import Client
from serializers import ClientSerializer

from rest_framework import viewsets

class ClientView():
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address', 'city', 'state', 'zip_code', 'country']

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer