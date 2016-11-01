from django.db import models

class Produce(models):
	
	produceId = models.IntegerField(primary_key=True, max_length=11)

	produceName = models.CharField(max_length=10)

	density = models.FloatField()

	water = models.FloatField()