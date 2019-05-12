from django.views.generic.base import TemplateView
from rest_framework import viewsets

from .models import Heart
from .serializers import HeartSerializer


class IndexView(TemplateView):

    template_name = "index.html"

class HeartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset=Heart.objects.all().order_by('-id')
    serializer_class=HeartSerializer
