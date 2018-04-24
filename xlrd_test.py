#!/usr/bin/python
#-*- coding: utf-8 -*-

from xlrd import open_workbook
x_data1=[]
y_data1=[]
wb = open_workbook('phase_detector.xlsx')
# 打开excel文件后，首先对文件内的sheet进行循环，这是最外层循环
for s in wb.sheets():
	print 'Sheet:', s.name
	# 在每个sheet内，进行第二次循环，行循环
	for row in range(s.nrows):
		print 'the row is:', row
		values = []
		# 列循环，取出行列值
		for col in range(s.ncols):
			values.append(s.cell(row,col).value)
		print values
		x_data1.append(values[0])
        y_data1.append(values[1])
