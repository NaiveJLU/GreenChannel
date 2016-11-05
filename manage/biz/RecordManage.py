from ..models.Record import Record
from ..models.User import User
from ..models.Produce import Produce
from ..models.Truck import Truck

from Result import failed, success
from django.core.exceptions import ObjectDoesNotExist
from config import file_url

def add_record(param):

	userId = param['user_id']
	driverName = param['driver_name']
	inStation = param['in_station']
	license = param['license']
	truckLoad = param['truck_load']
	truckForm = param['truck_form']
	startTime = param['start_time']
	isGreenChannel = param['is_green_channel']
	produceList = param['produce']

	# check user
	try:
		user = User.objects.get(userId=userId)
	except ObjectDoesNotExist:
		return failed(101)

	# check truck
	try:
		tk = Truck.objects.get(license=license)
	except ObjectDoesNotExist:
		tk = Truck.objects.create(license=license, truckForm=truckForm, truckLoad=truckLoad)


	errorList = []
	prodList = []
	for produceId in produceList:
		try:
			prodList.append(Produce.objects.get(produceId=produceId))
		except ObjectDoesNotExist:
			errorList.append(produceId)

	# produce error
	if len(errorList) > 0:
		return failed(102, 'error_produce', errorList)
	record = Record.objects.create(truck=tk,
						  driverName=driverName,
						  entryTime=startTime,
						  user=user,
						  isGreenChannel=isGreenChannel,
						  inStation=inStation, breakRule=False)
	for prod in prodList:
		record.produce.add(prod)
	record.save()
	return success('record_id', record.recordId)


def update_record(param):
	try:
		md_record = Record.objects.get(recordId=param['record_id'])

		if param['break_rule'] is not None:
			md_record.breakRule = param['break_rule']

		if param['scan_picture'] is not None:
			md_record.picturePath = param['scan_picture']

		md_record.save()

	except ObjectDoesNotExist:
		return failed(111)
	return success()

def find_record(param):
	recordId = param['record_id']
	try:
		record = Record.objects.get(recordId=recordId)
	except ObjectDoesNotExist:
		return failed(111)
	return success('record', record.to_dict())

def record_export(param):

	userId = param.get('user_id', None)
	startTime = param.get('start_time', None)
	endTime = param.get('end_time', None)
	inStation = param.get('in_station', None)
	breakRule = param.get('break_rule', None)
	isGreenChannel = param.get('is_green_channel', None)

	if breakRule is not None:
		breakRule = bool(int(breakRule))
	if isGreenChannel is not None:
		isGreenChannel = bool(int(isGreenChannel))
	print breakRule, isGreenChannel

	kwargs = {}
	if userId:
		kwargs['user__userId'] = userId
	if startTime and endTime:
		kwargs['entryTime__range'] = (startTime, endTime)
	if inStation:
		kwargs['inStation__contains'] = inStation
	if breakRule is not None:
		kwargs['breakRule__exact'] = breakRule
	if isGreenChannel is not None:
		kwargs['isGreenChannel__exact'] = isGreenChannel

	records = [ record for record in Record.objects.filter(**kwargs)]

	from Util import export_csv
	xid = export_csv(records)

	return success('path', file_url % xid)
