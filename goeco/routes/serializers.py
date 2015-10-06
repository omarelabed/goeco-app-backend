from models import Route
from rest_framework import serializers

class RouteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Route
		fields = ('co2', 'energy', 'id', 'km', 'reason', 'start_time', 'status', 'week', 'week_duration')
