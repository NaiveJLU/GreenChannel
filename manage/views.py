from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from biz import UserManage, ProduceManage, RecordManage
from biz import ProduceManage
import json

def GET_result(request, biz):
	param = request.GET
	res = biz(param)
	return HttpResponse(json.dumps(res), content_type='application/json')

def POST_result(request, biz):
	body = request.body
	param = json.loads(body)
	res = biz(param)
	return HttpResponse(json.dumps(res), content_type='application/json')

def index(request):
	#record = Record.objects.get(recordId=1)
	#return HttpResponse(json.dumps(record.to_dict()))
	return HttpResponse('success')

@csrf_exempt
def update_user(request):
	return POST_result(request, UserManage.update_user)

@csrf_exempt
def add_user(request):
	return POST_result(request, UserManage.add_user)

@csrf_exempt
def find_user(request):
	return GET_result(request, UserManage.find_user)

@csrf_exempt
def find_alluser(request):
	return GET_result(request, UserManage.find_alluser)

@csrf_exempt
def delete_user(request):
	return POST_result(request, UserManage.delete_user)

@csrf_exempt
def login(request):
	return POST_result(request, UserManage.login)

@csrf_exempt
def add_produce(request):
	return POST_result(request, ProduceManage.add_produce)

@csrf_exempt
def delete_produce(request):
	return POST_result(request, ProduceManage.delete_produce)

@csrf_exempt
def update_produce(request):
	return POST_result(request, ProduceManage.update_produce)

@csrf_exempt
def find_produce(request):
	return GET_result(request, ProduceManage.find_produce)

@csrf_exempt
def find_allproduce(request):
	return GET_result(request, ProduceManage.find_allproduce)

@csrf_exempt
def find_record(request):
	return GET_result(request, RecordManage.find_record)

@csrf_exempt
def add_record(request):
	return POST_result(request, RecordManage.add_record)

@csrf_exempt
def update_record(request):
	return POST_result(request, RecordManage.update_record)

@csrf_exempt
def record_export(request):
	return GET_result(request, RecordManage.record_export)
