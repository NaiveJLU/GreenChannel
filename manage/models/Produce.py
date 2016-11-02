from django.db import models

class Produce(models.Model):
	
	produceId = models.AutoField(primary_key=True, auto_created=True, max_length=11)

	produceName = models.CharField(max_length=10, unique=True)

	density = models.FloatField()

	water = models.FloatField()