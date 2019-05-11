from rest_framework import viewsets
from .models import Heart 
from .serializers import HeartSerializer


class HeartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Heart.objects.all().order_by('-id')
    serializer_class = HeartSerializer



