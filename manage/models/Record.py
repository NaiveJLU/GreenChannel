from django.db import models
from ..models.Truck import Truck
from ..models.User import User

class Record(models.Model):

	recordId = models.AutoField(primary_key=True, max_length=11)

	truckId = models.ForeignKey(Truck, on_delete=models.CASCADE)

	driverName = models.CharField(max_length=30)

	entryTime = models.DateTimeField()

	user = models.ForeignKey(User, on_delete=models.CASCADE)

	isCreenChannel = models.BooleanField()

	inStation = models.CharField(max_length=15)

	outStation = models.CharField(max_length=15)

	picturePath = models.CharField(max_length=100, null=True)

	breakRule = models.BooleanField(null=True)

	def to_dict(self):
		return {
			"record_id": self.recordId,
			"start_time": str(self.entryTime),
			"in_station": self.inStation,
			"user_id": 123,
			"break_rule": self.breakRule,
			"is_green_channel": self.isCreenChannel,
			"truck": self.truckId.to_dict(),
			"produce": []
		}

