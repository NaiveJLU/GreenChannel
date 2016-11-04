# coding: utf-8
from django.db import models
from ..models.Truck import Truck
from ..models.User import User
from ..models.Produce import Produce

class Record(models.Model):

	recordId = models.AutoField(primary_key=True, max_length=11)

	truck = models.ForeignKey(Truck, on_delete=models.CASCADE)

	driverName = models.CharField(max_length=30)

	entryTime = models.DateTimeField()

	user = models.ForeignKey(User, on_delete=models.CASCADE)

	isGreenChannel = models.BooleanField()

	inStation = models.CharField(max_length=15)

	outStation = models.CharField(max_length=15)

	picturePath = models.CharField(max_length=100, null=True)

	breakRule = models.BooleanField(null=True)

	produce = models.ManyToManyField(Produce)

	def to_dict(self):
		return {
			"record_id": self.recordId,
			"start_time": str(self.entryTime),
			"in_station": self.inStation,
			"user_id": self.user.userId,
			"break_rule": self.breakRule,
			"is_green_channel": self.isGreenChannel,
			"truck": self.truck.to_dict(),
			"produce": [p.to_dict() for p in self.produce.all()]
		}
	def to_csv(self):
		return (
			self.recordId,
			'是'.decode('utf-8') if self.breakRule else '否'.decode('utf-8'),
			'是'.decode('utf-8') if self.isGreenChannel else '否'.decode('utf-8'),
			''.join([p.produceName + ' ' for p in self.produce.all()]),
			self.user.username,
			self.user.name,
			self.truck.license,
			self.truck.truckForm,
			self.truck.truckLoad,
			str(self.entryTime),
			self.inStation
		)
