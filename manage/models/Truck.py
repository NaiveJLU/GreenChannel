from django.db import models

class Truck(models.Model):

	# truck primary key
	truckId = models.AutoField(primary_key=True, max_length=11)

	# license
	license = models.CharField(max_length=12)

	# truck form a/b/c
	truckForm = models.CharField(max_length=1)

	# truck weight
	truckLoad = models.FloatField()

	def to_dict(self):
		return {
			"truck_id" : self.truckId,
			"license" : self.license.encode('utf-8'),
			"truck_load" : self.truckLoad,
			"truck_form" : self.truckForm
		}