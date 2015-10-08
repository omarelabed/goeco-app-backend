from models import Route, Activity
from rest_framework import serializers


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Activity
		fields = ('activityMoves','activityMoves','activity','validated','startTime','endTime','duration','distance','trackPoints')

class RouteSerializer(serializers.HyperlinkedModelSerializer):
	activities = ActivitySerializer(many=True)
	class Meta:
		model = Route
		fields = ('startTime', 'endTime', 'co2', 'energy', 'activities')
		depth = 1
