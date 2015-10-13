from django.contrib.auth.models import Group
from models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'url')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    users = UserSerializer(many=True)

    class Meta:
        model = Group
        fields = ('url', 'name', 'id', 'users')


class TrackPointSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = TrackPoint
        fields = ('activity', 'lat', 'lon', 'time')


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    trackPoints = TrackPointSerializer(many=True)

    class Meta:
        model = Activity
        fields = ('url', 'activityMoves', 'activityMoves', 'validated',
                  'startTime', 'endTime', 'duration', 'distance', 'trackPoints', 'id')


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    activities = ActivitySerializer(many=True)
    id = serializers.ReadOnlyField()

    class Meta:
        model = Route
        fields = ('url', 'startTime', 'endTime', 'co2', 'energy', 'activities', 'id')
        depth = 1


class ReasonViewSerializer(serializers.HyperlinkedModelSerializer):
    route = RouteSerializer()
    id = serializers.ReadOnlyField()

    class Meta:
        model = Reason
        fields = ('description', 'route', 'id')
        depth = 0


class WeekSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    routes = RouteSerializer(many=True)
    """
    GoEco! week.
    """
    class Meta:
        model = Week
        fields = ('url', 'name', 'validated', 'routes', 'id')


class UserSettingsSerializer(serializers.HyperlinkedModelSerializer):
    """
    GoEco! user settings.
    """
    class Meta:
        model = UserSettings
        fields = ('url', 'notifications', 'car_owner')
        depth = 1


class GoEcoAccountSerializer(serializers.HyperlinkedModelSerializer):
    weeks = WeekSerializer(many=True)
    user_settings = UserSettingsSerializer(required=False)
    user = UserSerializer()
    id = serializers.ReadOnlyField()

    class Meta:
        model = GoEcoAccount
        fields = ('url', 'user', 'weeks', 'id', 'user_settings')
        depth = 3

    def create(self, validated_goecoaccount):
        print "ciao"
        profile_data = validated_goecoaccount.pop('profile')
        weeks_data = validated_goecoaccount.pop('weeks')
        user = User.objects.create(**validated_goecoaccount)
        user_settings = None
        # GoEcoAccount.objects.create(user=user, weeks=weeks_data, usersettings=usersettings)
        return None
