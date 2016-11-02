from ..models.User import User
from django.db import IntegrityError
from Result import failed, success
from django.core.exceptions import ObjectDoesNotExist
def add_user(user):

	try:
		User.objects.create(username=user['username'],
							password=user['password'],
							name=user['name'],
							gender=user['gender'],
							title=user['title'],
							birthday=user['birthday'])

		return failed(100)

	except IntegrityError:
		return failed(161)

def delete_user(userId):
	pass

def update_user(user):
	try:
		md_user = User.objects.get(userId=user['user_id'])

		if user['username'] is not None:
			md_user.username = user['username']

		if user['password'] is not None:

			md_user.password = user['password']

		if user['name'] is not None:
			md_user.name = user['name']

		if user['gender'] is not None:
			md_user.gender = user['gender']

		if user['title'] is not None:
			md_user.title = user['title']

		if user['birthday'] is not None:
			md_user.birthday = user['birthday']
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

