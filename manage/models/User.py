from django.db import models


class User(models.Model):

	# user id
	userId = models.IntegerField(primary_key=True, auto_created=True, max_length=11)

	# username
	username = models.CharField(max_length=20)

	# password
	password = models.CharField(max_length=20)

	# name of user
	name = models.CharField(max_length=20)

	# sex of user
	gender = models.BooleanField()

	# title : {1 : checker, 0 : manager}
	title = models.BooleanField()

	#birthday
	birthday = models.DateField()