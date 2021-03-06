error_message = {
	100 : 'SUCCESS',
	101 : 'USER_NOT_EXIST',
	102 : 'PRODUCE_NOT_EXIST',
	111 : 'RECORD_NOT_EXIST',
	131 : 'USERNAME_NOT_EXIST',
	132 : 'PASSWORD_NOT_MATCHED',
	133 : 'SERVER_INTERNAL_ERROR',
	141 : 'PRODUCE_NOT_EXIST',
	151 : 'INVALID_USER_ID',
	161 : 'USER_EXIST',
	171 : 'PRODUCE_EXIST',
}

def failed(errorCode, key=None, obj=None):
	if key is not None:
		return {
			'success': True if errorCode == 100 else False,
			'code': errorCode,
			'message': error_message[errorCode],
			key : obj
		}

	else:
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