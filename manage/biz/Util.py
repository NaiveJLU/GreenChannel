# coding: utf-8

from datetime import datetime
import xlsxwriter

file_base = 'C:\\Users\\Prince\\'

def random_str(length=8):
	import random
	chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
	return ''.join([chars[random.randint(0, len(chars) - 1)] for i in xrange(length)])

def get_file_name():
	time = datetime.now()
	return "%04d%02d%02d%02d%02d%02d_%s.xlsx" % (time.year, time.month, time.day, \
												time.hour, time.minute, time.second, random_str(4))\

def export_csv(records):
	xlsxName = get_file_name()
	workbook = xlsxwriter.Workbook(file_base + xlsxName)
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
					'进站口'.decode('utf-8')))
	row = 2
	for record in records:
		worksheet.write_row('A' + str(row), record.to_csv())
		row += 1
	workbook.close()
	return xlsxName
