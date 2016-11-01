error_message = {
	100 : 'SUCCESS',
	131 : 'USERNAME_NOT_EXIST',
	132 : 'PASSWORD_NOT_MATCHED',
	151 : 'INVALID_USER_ID',
	161 : 'USER_EXIST'
}

def failed(errorCode):

	return {
		'success' : True if errorCode == 100 else False,
		'code' : errorCode,
		'message' : error_message[errorCode]
	}

def success(key=None, obj=None):
	if key is not None:
		return {
			'success': True,
			'code': 100,
			'message': 'SUCCESS',
			key : obj
		}
	else :
		return {
			'success': True,
			'code': 100,
			'message': 'SUCCESS'
		}