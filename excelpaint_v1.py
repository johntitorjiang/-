#!/usr/bin/python
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import xlrd
from xlrd import open_workbook
from pylab import *

# 增加三组数据和理想数据
x_data=[]
y_data=[]
x_data1=[]
y_data1=[]
x_data2=[]
y_data2=[]
x_data3=[]
y_data3=[]
x_volte=[]
temp=[]

# 打开excel文件
wb = open_workbook('phase_detector.xlsx')

for s in wb.sheets():
    print 'Sheet:',s.name
# 在每个sheet内，进行第二次循环，行循环
    for row in range(s.nrows):
        print 'the row is:',row
        values = []
		# 列循环，取出行列值
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print values
        x_data.append(values[0]/180.0)
        y_data.append(values[1])  

wb = open_workbook('phase_detector2.xlsx')
for s in wb.sheets():
    print 'Sheet:',s.name
    for row in range(s.nrows):
        print 'the row is:',row
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print values
        x_data2.append(values[0]/180.0)
        y_data2.append(values[1])

# 理想曲线数据
for i in range(360):
    x_data3.append(i/180.0)
    y_data3.append((i-180)*0.052-0.092)
	
# plt.plot(x轴数据, y轴数据, 曲线类型,图例说明,曲线线宽)
plt.plot(x_data, y_data, 'bo--', label=u"Faster D latch and XOR", linewidth=2)
plt.plot(x_data2, y_data2, 'r-.',label=u"Move the pullup resistor",linewidth=2)
plt.plot(x_data3, y_data3, 'c',label=u"The Ideal Curve",linewidth=2)

# plt.annotate(标注文字, 标注的数据点, 标注文字坐标, 箭头形状)
# plt.annotate('zero point', xy=(180,0), xytext=(60,3), arrowprops=dict(facecolor='black', shrink=0.05),)
# 零点
plt.annotate('The favorite close loop point',size=16, xy=(1, 0.1), xycoords='data',
                xytext=(-180, 40), textcoords='offset points',
                arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2")
                )
# 非单调区域的零点
plt.annotate(' ', xy=(0.02, -0.2), xycoords='data',
                xytext=(200, -90), textcoords='offset points',
                arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=-.2")
                )
plt.annotate('Zero point in non-monotonic region', size=16,xy=(1.97, -0.3), xycoords='data',
                xytext=(-290, -110), textcoords='offset points',
                arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2")
                )

# 图片顶部的名称
plt.title(u"$2\pi$ phase detector",size=20)
# plt.title(u"Excel Paint v1")
# 显示label
plt.legend(loc=0)

# 坐标轴移动
ax = gca()
# 设置右边界不可见
ax.spines['right'].set_color('none')
# 设置上边界不可见
ax.spines['top'].set_color('none')
# 左边界(y轴)下边界(x轴)零点对应
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# x, y轴数据名
plt.xlabel(u"$\phi/rad$",size=20)
plt.ylabel(u"$DC/V$",size=20)
# 坐标轴单位更改
plt.xticks([0, 0.5, 1, 1.5, 2],
		   [r'$0$', r'$\pi/2$', r'$\pi$', r'$1.5\pi$', r'$2\pi$'],size=16)

# 图像与坐标轴相交部分透明
for label in ax.get_xticklabels() + ax.get_yticklabels():
    #label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))
	
plt.grid(True)

plt.show()
print 'over!'