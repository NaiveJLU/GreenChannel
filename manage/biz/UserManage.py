from ..models.User import User
from django.db import IntegrityError
from Result import failed, success

def add_user(user):

	try:
		User.objects.create(userName=user['userName'],
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
	pass

def find_user(userId):
	pass

def login(username, password):

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

