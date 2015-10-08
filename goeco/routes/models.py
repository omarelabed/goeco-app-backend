from django.contrib.auth.models import User
from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField


class EcoUser(models.Model):
	##IDSIA
	# {  
	user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL);
	#     "userId":"userId1",
	# TODO
	#     "username":"pinco pallino",
	username = models.CharField(max_length=200)
	#     "weeks":[ ... ]
	weeks = ListField(EmbeddedModelField('Week'))
	# }
	##/IDSIA

class UserSettings(models.Model):
	ecouser = EmbeddedModelField('EcoUser')

class Week(models.Model):
	##IDSIA
	# {  
	#     "weekId":"weekId1",
	# TODO
	#     "name":"Week 1",
	name = models.CharField(max_length=200)
	#     "validated":false,
	validated = models.BooleanField()
	#     "days":[ ... ]
	days = ListField(EmbeddedModelField('Day'))
	# },
	##/IDSIA

class Day(models.Model):
	##IDSIA
	# {
	#     "dayId":"dayId1",
	# TODO
	#     "name":"Monday",
	name = models.CharField(max_length=200)
	#     "validated":false,
	validated = models.BooleanField()
	#     "routes":[ ... ]
	routes = ListField(EmbeddedModelField('Route'))
	# },
	##/IDSIA

class Route(models.Model):
	##LOCAL
	# id

	# user_id
	user = EmbeddedModelField('User')
	##/LOCAL

	##IDSIA
	# {
	#     "startTime":"20121212T071430+0200",
	startTime = models.DateTimeField('date published')
	#     "endTime":"20121212T074617+0200",
	endTime = models.DateTimeField('date published')
	#     "co2":20,
	co2 = models.PositiveIntegerField()	
	#     "energy":10,
	energy = models.PositiveIntegerField()
	#     "activities":[ ... ]
	activities = ListField(EmbeddedModelField('Activity'))
	# }
	##/IDSIA

class Reason(models.Model):
	route = models.OneToOneField(Route, blank=True, null=True, on_delete=models.SET_NULL)
	description = models.CharField(max_length=200)

class Activity(models.Model):
	##IDSIA
	# {  
	#     "activityMoves":"walking",
	activityMoves = models.CharField(max_length=200)
	#     "activityIDSIA":"walking",
	activityMoves = models.CharField(max_length=200)
	#     "activity":"walking",
	activity = models.CharField(max_length=200)
	#     "validated":true,
	validated = models.BooleanField()
	#     "startTime":"20121212T071430+0200",
	startTime = models.DateTimeField()
	#     "endTime":"20121212T072732+0200",
	endTime = models.DateTimeField()
	#     "duration":782,
	duration = models.IntegerField()
	#     "distance":1251,
	distance = models.IntegerField()
	#     "trackPoints":[ ... ]
	trackPoints = ListField(EmbeddedModelField('TrackPoint'))
	# },
	##/IDSIA

class TrackPoint(models.Model):
	##IDSIA
	# {  
	#     "lat":55.55555,
	lat = models.FloatField()
	#     "lon":33.33333,
	lon = models.FloatField()
	#     "time":"20121212T071430+0200"
	time = models.DateTimeField()
	# },
	##/IDSIA
