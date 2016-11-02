from ..models.User import User
from django.db import IntegrityError
from Result import failed, success
from django.core.exceptions import ObjectDoesNotExist
def add_user(param):

	try:
		user = User.objects.create(username=param['username'],
							password=param['password'],
							name=param['name'],
							gender=param['gender'],
							title=param['title'],
							birthday=param['birthday'])
		return success('user_id', user.userId)

	except IntegrityError:
		return failed(161)

def delete_user(param):
	try:
		user = User.objects.get(userId=param['user_id'])
	except ObjectDoesNotExist:
		return failed(151)
	user.delete()
	return success()

def update_user(param):
	try:
		md_user = User.objects.get(userId=param['user_id'])

		if param['username'] is not None:
			md_user.username = param['username']

		if param['password'] is not None:

			md_user.password = param['password']

		if param['name'] is not None:
			md_user.name = param['name']

		if param['gender'] is not None:
			md_user.gender = param['gender']

		if param['title'] is not None:
			md_user.title = param['title']

		if param['birthday'] is not None:
			md_user.birthday = param['birthday']
		md_user.save()

	except ObjectDoesNotExist:
		return failed(151)
	return success()


def find_user(param):
	userId = param['user_id']
	try:
		user = User.objects.get(userId=userId)
	except ObjectDoesNotExist:
		return failed(151)
	return success('user', {
		'user_id' : user.userId,
		'username': user.username,
		'name': user.name,
		'gender': user.gender,
		'title': user.title,
		'birthday': str(user.birthday)
	})

def login(param):

	username = param['username']
	password = param['password']

	try:
		user = User.objects.get(username=username)
	except:
		return failed(131)

	if password != user.password:
		return failed(132)

	return success('user', {
		"userId": user.userId,
		"userName": user.username,
		"name": user.name,
		"gender": user.gender,
		"title": user.title,
		"birthday": str(user.birthday)
	})

