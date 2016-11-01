from datetime import date
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from biz import UserManage
from models.User import User
import json

def index(request):
	user = User.objects.get(userName='prince')
	return HttpResponse(user.password)

@csrf_exempt
def add_user(request):
	body = request.body
	req = json.loads(body)
	res = UserManage.add_user(req)
	return HttpResponse(json.dumps(res), content_type='application/json')

@csrf_exempt
def login(request):
	body = request.body
	req = json.loads(body)
	username = req['username']
	password = req['password']
	return HttpResponse(json.dumps(UserManage.login(username, password)), content_type='application/json')

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