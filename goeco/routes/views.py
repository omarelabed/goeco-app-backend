from models import Route, Activity
from rest_framework import viewsets
from routes.serializers import RouteSerializer, ActivitySerializer

class RouteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Route.objects.all().select_related('activity')
    serializer_class = RouteSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
