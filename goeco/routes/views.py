from models import *
from rest_framework import viewsets
from routes.serializers import *
# import pdb;


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GoEcoAccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows GoEco! users to be viewed or edited.
    """
    queryset = GoEcoAccount.objects.all()#.select_related('weeks')
    serializer_class = GoEcoAccountSerializer


class UserSettingsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows GoEco! users to be viewed or edited.
    """
    queryset = UserSettings.objects.all()#.select_related('goecoaccount')
    serializer_class = UserSettingsSerializer


class WeekViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows GoEco! weeks to be viewsed or edited.
    """
    queryset = Week.objects.all()#.select_related('week')
    serializer_class = WeekSerializer


class RouteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows routes to be viewed or edited.
    """
    queryset = Route.objects.all()#.select_related('activity')
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
