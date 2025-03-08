from maBE.models import Client
from maBE.serializers import ClientSerializer

from rest_framework import viewsets

class ClientViewSet(viewsets.ModelViewSet):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address', 'city', 'state', 'zip_code', 'country']
        
    queryset = Client.objects.all()
    serializer_class = ClientSerializer 