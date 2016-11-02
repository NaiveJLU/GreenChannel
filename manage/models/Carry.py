from django.db import models
from Produce import Produce
from Record import Record
class Carry(models.Model):

	produceId = models.ForeignKey(Produce)

	recordId = models.ForeignKey(Record)