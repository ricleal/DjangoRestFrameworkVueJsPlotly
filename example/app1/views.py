from django.views.generic.base import TemplateView
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

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

    @list_route()
    def age_desease(self, request):
        q = self.get_queryset().values('age', 'presence_of_heart_disease')
        return Response(list(q))
