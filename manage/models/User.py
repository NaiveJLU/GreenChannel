from django.db import models


class User(models.Model):

	# user id
	userId = models.AutoField(primary_key=True, auto_created=True, max_length=11)

	# username
	username = models.CharField(max_length=20, unique=True)

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

	def to_dict(self):
		return {
			'user_id': self.userId,
			'username': self.username,
			'name': self.name.encode('utf-8'),
			'gender': self.gender,
			'title': self.title,
			'birthday': str(self.birthday)
		}