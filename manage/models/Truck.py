from django.db import models

class Truck(models):

	# truck primary key
	truckId = models.IntegerField(primary_key=True, max_length=11)

	# license
	license = models.CharField(max_length=12)

	# truck form a/b/c
	truckForm = models.CharField(max_length=1)

	# truck weight
	truckLoad = models.FloatField()