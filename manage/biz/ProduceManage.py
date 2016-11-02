from ..models.Produce import Produce
from django.db import IntegrityError
from Result import failed, success
from django.core.exceptions import ObjectDoesNotExist

def add_produce(param):

	try:
		produce = Produce.objects.create(
							produceName=param['produce_name'],
							density=param['density'],
							water=param['water'])

		return success('produce_id', produce.produceId)

	except IntegrityError:
		return failed(171)

def delete_produce(param):
	try:
		produce = Produce.objects.get(produceId=param['produce_id'])
	except ObjectDoesNotExist:
		return failed(141)
	produce.delete()
	return success()

def update_produce(param):
	try:
		md_produce = Produce.objects.get(produceId=param['produce_id'])

		if param['produce_name'] is not None:
			md_produce.produceName = param['produce_name']

		if param['density'] is not None:

			md_produce.density = param['density']

		if param['water'] is not None:
			md_produce.water = param['water']

		md_produce.save()

	except ObjectDoesNotExist:
		return failed(141)
	return success()


def find_produce(param):
	produceId = param['produce_id']
	try:
		produce = Produce.objects.get(produceId=produceId)
	except ObjectDoesNotExist:
		return failed(141)
	return success('produce', produce.to_dict())

def find_allproduce(param):
	try:
		produce_list = [produce.to_dict() for produce in Produce.objects.all()]
		return success('produce', produce_list)
	except :
		return failed(133)