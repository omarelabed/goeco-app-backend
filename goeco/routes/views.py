from models import Route
from rest_framework import viewsets
from routes.serializers import RouteSerializer

class RouteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
