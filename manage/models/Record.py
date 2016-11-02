from django.db import models
from ..models import Truck
from ..models import User

class Record(models.Model):

	recordId = models.AutoField(primary_key=True, max_length=11)

	truckId = models.ForeignKey(Truck, on_delete=models.CASCADE)

	driverName = models.CharField(max_length=30)

	entryTime = models.DateTimeField()

	userId = models.ForeignKey(User, on_delete=models.CASCADE)

	isCreenChannel = models.BooleanField()

	inStation = models.CharField(max_length=15)

	outStation = models.CharField(max_length=15)

	picturePath = models.CharField(max_length=100, null=True)

	breakRule = models.BooleanField(null=True)

