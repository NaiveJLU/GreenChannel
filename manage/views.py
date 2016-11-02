from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from biz import UserManage
from django.core.exceptions import ObjectDoesNotExist
from models.User import User
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
	param = request.GET


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
def login(request):
	return POST_result(request, UserManage.login)

@csrf_exempt
def test_login(request):
	body = request.body
	req = json.loads(body)
	username = req['username']
	password = req['password']
	if username == 'ydc' and password == '123':
		ret = {
			"success": True,
			"code": 100,
			"message": "success",
			"user":
				{
					"userId": 123,
					"userName": "zhangsan",
					"password": "dfajdsafsfjidsoajawie",
					"name": "zhangsan",
					"gender": 0,
					"title": 1,
					"birthday": "1994-08-23",
				}
		}
		return HttpResponse(json.dumps(ret), content_type='application/json')

	error = {
		"success": False,
		"code": 131,
		"message": "USERNAME_NOT_EXIST",
	}
	return HttpResponse(json.dumps(error), content_type='application/json')