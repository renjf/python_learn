#!/usr/bin/python
#_*_coding:utf-8_*_
import os
import xlrd
import sys
import re
import xlwt
print 'welcome to my world'

file = xlwt.Workbook() #注意这里的Workbook首字母是大写，无语吧

#新建一个sheet

table = file.add_sheet(u'Bug和Patch对应表')

#写入数据table.write(行,列,value)

table.write(0,0,'Bug')
table.write(0,1,'Patch')
table.write(0,2,'Package')
table.write(0,3,'Remark')


#如果对一个单元格重复操作，会引发
#returns error:
# Exception: Attempt to overwrite cell:
# sheetname=u'sheet 1' rowx=0 colx=0

#所以在打开时加cell_overwrite_ok=True解决

#table = file.add_sheet('sheet name',cell_overwrite_ok=True)

#保存文件

file.save('demo2.xls')
