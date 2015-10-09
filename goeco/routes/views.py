from django.contrib.auth.models import User
from models import *
from rest_framework import viewsets
from routes.serializers import *

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class EcoUserViewSet(viewsets.ModelViewSet):
	"""
    API endpoint that allows GoEco! users to be viewed or edited.
	"""
	queryset = EcoUser.objects.all().select_related('weeks')
	serializer_class = EcoUserSerializer

class UserSettingsViewSet(viewsets.ModelViewSet):
	"""
    API endpoint that allows GoEco! users to be viewed or edited.
	"""
	queryset = UserSettings.objects.all().select_related('ecouser')
	serializer_class = UserSettingsSerializer

class WeekViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows GoEco! weeks to be viewsed or edited.
	"""
	queryset = Week.objects.all().select_related('week')
	serializer_class = WeekSerializer		

class DayViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows GoEco! days to be viewsed or edited.
	"""
	queryset = Day.objects.all().select_related('day')
	serializer_class = DaySerializer		

class RouteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows routes to be viewed or edited.
    """
    queryset = Route.objects.all().select_related('activity')
    serializer_class = RouteSerializer

class ReasonViewSet(viewsets.ModelViewSet):
	"""
    API endpoint that allows reasons to be viewed or edited.
	"""
	queryset = Reason.objects.all()
	serializer_class = ReasonViewSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows activities to be viewed or edited.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
