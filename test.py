import xlrd
import xlwt as xlwt

data=xlwt.Workbook()

table=data.add_sheet('name')
table.write(0,0,u'呵呵')
table.write(0,1,u'呵呵')

data.save('test.xls')