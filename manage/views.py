
from models.Student import Student
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
def index(request):
	stu = Student.objects.get(name='hehe')
	return HttpResponse(str(stu.name) + str(stu.age))

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