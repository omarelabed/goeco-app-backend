from models import *
from rest_framework import serializers


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Activity
		fields = ('url', 'activityMoves','activityMoves','activity','validated','startTime','endTime','duration','distance','trackPoints')

class RouteSerializer(serializers.HyperlinkedModelSerializer):
	activities = ActivitySerializer(many=True)
	class Meta:
		model = Route
		fields = ('url', 'startTime', 'endTime', 'co2', 'energy', 'activities')
		depth = 1

class ReasonViewSerializer(serializers.HyperlinkedModelSerializer):
	route = RouteSerializer()
	class Meta:
		model = Reason
		fields = ('description', 'route')
		depth = 0

class DaySerializer(serializers.HyperlinkedModelSerializer):
	routes = RouteSerializer(many=True, read_only=True)
	"""
	GoEco! day.
	"""
	class Meta:
		model = Day
		fields = ('name', 'validated', 'routes')

class WeekSerializer(serializers.HyperlinkedModelSerializer):
	days = DaySerializer(many=True, read_only=True)
	"""
	GoEco! week.
	"""
	class Meta:
		model = Week
		fields = ('url', 'name', 'validated', 'days')

class EcoUserSerializer(serializers.HyperlinkedModelSerializer):
	weeks = WeekSerializer(many=True)
	class Meta:
		model = EcoUser
		fields = ('url', 'user', 'username', 'weeks')
		depth = 3

class UserSettingsSerializer(serializers.HyperlinkedModelSerializer):
	ecouser = EcoUserSerializer()
	"""
	GoEco! user settings.
	"""
	class Meta:
		model = UserSettings
		fields = ('ecouser')
		depth = 1