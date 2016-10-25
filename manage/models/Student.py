from django.db import models


class Student(models.Model):

	name = models.CharField(max_length=30)
	age = models.IntegerField(primary_key=True, max_length=10)

