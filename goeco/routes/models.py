from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField

class Activity(models.Model):
	##IDSIA
	#       {  
	#          "activityMoves":"walking",
	activityMoves = models.CharField(max_length=200)
	#          "activityIDSIA":"walking",
	activityMoves = models.CharField(max_length=200)
	#          "activity":"walking",
	activity = models.CharField(max_length=200)
	#          "validated":true,
	validated = models.BooleanField()
	#          "startTime":"20121212T071430+0200",
	startTime = models.DateTimeField()
	#          "endTime":"20121212T072732+0200",
	endTime = models.DateTimeField()
	#          "duration":782,
	duration = models.IntegerField()
	#          "distance":1251,
	distance = models.IntegerField()
	#          "trackPoints":[ ... ]
	trackPoints = ListField(EmbeddedModelField('TrackPoint'))
	#       },
	##/IDSIA


class TrackPoint(models.Model):
	##IDSIA
	#             {  
	#                "lat":55.55555,
	lat = models.FloatField()
	#                "lon":33.33333,
	lon = models.FloatField()
	#                "time":"20121212T071430+0200"
	time = models.DateTimeField()
	#             },
	##/IDSIA


class Route(models.Model):
	##LOCAL
	# id

	# user_id
	user = EmbeddedModelField('User')
	##/LOCAL

	##IDSIA
	# {
	#    "startTime":"20121212T071430+0200",
	startTime = models.DateTimeField('date published')
	#    "endTime":"20121212T074617+0200",
	endTime = models.DateTimeField('date published')
	#    "co2":20,
	co2 = models.PositiveIntegerField()	
	#    "energy":10,
	energy = models.PositiveIntegerField()
	#    "activities":[ ... ]
	activities = ListField(EmbeddedModelField('Activity'))
	# }
	##/IDSIA
