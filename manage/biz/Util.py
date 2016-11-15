# coding: utf-8

import xlsxwriter
import base64
from datetime import datetime
from config import file_base, img_base

def readFile(path, buf_size=262144):

	f = open(path, "rb")
	while True:
		c = f.read(buf_size)
		if c:
			yield c
		else:
			break
	f.close()

def random_str(length=8):
	import random
	chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
	return ''.join([chars[random.randint(0, len(chars) - 1)] for i in xrange(length)])

def get_file_name():
	time = datetime.now()
	return "%04d%02d%02d%02d%02d%02d_%s" % (time.year, time.month, time.day, \
												time.hour, time.minute, time.second, random_str(4))\

def export_csv(records):
	xlsxName = get_file_name()
	workbook = xlsxwriter.Workbook(file_base + xlsxName + '.xlsx')
	worksheet = workbook.add_worksheet()

	worksheet.write_row('A1',('记录编号'.decode('utf-8'),
					'是否违规'.decode('utf-8'),
					'是否绿通'.decode('utf-8'),
					'农产品'.decode('utf-8'),
					'报关员用户名'.decode('utf-8'),
					'报关员姓名'.decode('utf-8'),
					'货车车牌'.decode('utf-8'),
					'货车车型'.decode('utf-8'),
					'货车车重'.decode('utf-8'),
					'进站时间'.decode('utf-8'),
					'进站口'.decode('utf-8')),
					'图片'.decode('utf-8'))
	row = 2
	for record in records:
		worksheet.write_row('A' + str(row), record.to_csv())
		worksheet.insert_image('L' + str(row), img_base + record.picturePath,
							   {'x_scale': 0.3,
								'y_scale': 0.1,
								'positioning': 1
								})
		row += 1
	workbook.close()
	return xlsxName

def save_image(b64):
	file_name = get_file_name() + '.bmp'
	base64_decode(b64, file_name)
	return file_name

def base64_decode(b64, file_name):
	png = base64.b64decode(b64)
	out = open(img_base + file_name, 'wb')
	out.write(png)
	out.close()
