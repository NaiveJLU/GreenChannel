error_message = {
	100 : 'SUCCESS',
	131 : 'USERNAME_NOT_EXIST',
	132 : 'PASSWORD_NOT_MATCHED',
	161 : 'USER_EXIST'
}

def failed(errorCode):

	return {
		'success' : True if errorCode == 100 else False,
		'code' : errorCode,
		'message' : error_message[errorCode]
	}

def success(key, obj):

	return {
		'success': True,
		'code': 100,
		'message': 'SUCCESS',
		key : obj
	}