
from models.Student import Student
from django.http import HttpResponse

def index(request):
	stu = Student.objects.get(name='hehe')
	return HttpResponse(str(stu.name) + str(stu.age))

