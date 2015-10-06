from django.db import models

class Route(models.Model):
	# id
	# TODO
	# user_id
	# user = models.ForeignKey(User)

	# km
	km = models.PositiveIntegerField()
	
	# start_time date
	start_time = models.DateTimeField('date published')

	# week
	week = models.PositiveIntegerField()

	# duration
	week_duration = models.PositiveIntegerField()

	# co2
	co2 = models.PositiveIntegerField()
	
	# energy
	energy = models.PositiveIntegerField()

	# reason
	reason = models.CharField(max_length=200)

	# means
	# TODO: vedere se conviene avere un model dedicato ai means
	reason = models.CharField(max_length=200)

	# status
	# TODO: vedere se conviene avere un model dedicato agli status
	# 		(per selezionare da piu' opzioni, assegnare colori, ecc.)
	status = models.CharField(max_length=200)

	# path gmap ??
	# TODO: ??
