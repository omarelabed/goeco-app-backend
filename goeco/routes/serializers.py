from models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.ReadOnlyField()
	class Meta:
		model = Activity
		fields = ('url', 'activityMoves','activityMoves','activity','validated','startTime','endTime','duration','distance','trackPoints', 'id')

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

class DaySerializer(serializers.HyperlinkedModelSerializer):
	routes = RouteSerializer(many=True, read_only=True)
	id = serializers.ReadOnlyField()
	"""
	GoEco! day.
	"""
	class Meta:
		model = Day
		fields = ('name', 'validated', 'routes', 'id')

class WeekSerializer(serializers.HyperlinkedModelSerializer):
	days = DaySerializer(many=True, read_only=True)
	id = serializers.ReadOnlyField()
	"""
	GoEco! week.
	"""
	class Meta:
		model = Week
		fields = ('url', 'name', 'validated', 'days', 'id')

class EcoUserSerializer(serializers.HyperlinkedModelSerializer):
	weeks = WeekSerializer(many=True)
	id = serializers.ReadOnlyField()
	class Meta:
		model = EcoUser
		fields = ('url', 'user', 'username', 'weeks', 'id')
		depth = 3

class UserSettingsSerializer(serializers.HyperlinkedModelSerializer):
	ecouser = EcoUserSerializer()
	id = serializers.ReadOnlyField()
	"""
	GoEco! user settings.
	"""
	class Meta:
		model = UserSettings
		fields = ('ecouser', 'id')
		depth = 1