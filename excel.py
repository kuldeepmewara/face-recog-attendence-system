# Writing to an excel 
# sheet using Python 
'''
import xlwt 
from xlwt import Workbook 

# Workbook is created 
wb = Workbook() 

# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 

header=['college','branch','year','date1','date2','date3']

names=['priyanka','kangana','kuldeep']

for i in range(len(header)):
  sheet1.write( 0,i,header[i]) 


wb.save('attendence.xls') 
'''
import datetime



import xlwings 
now=datetime.datetime.now()
d=now.strftime("%d-%m-%Y")

t=now.strftime("%I:%M")
print(t)
week_no=now.strftime("%w")
print(week_no)

if week_no in [3,6]:
   print("yes")
 

def record(id):

 now=datetime.datetime.now()
 d=now.strftime("%d-%m-%Y")
 week_no=now.strftime("%w")


 t=now.strftime("%I:%M")
 print(t)
 
 
 holiday=[0,6]

 dates=['05-06-2019','06-06-2019','07-06-2019','08-06-2019','09-06-2019','10-06-2019','11-06-2019',	'12-06-2019','13-06-2019','14-06-2019','15-06-2019','16-06-2019','17-06-2019','18-06-2019','19-06-2019','20-06-2019']

 date_index=dates.index(d)+4

 wb = xlwings.Book("attendence.xls") 

 Sheet1 = wb.sheets[0]
 
 if week_no not in holiday:
  Sheet1.range(id,date_index).value = t #This will change the cell(2,4) to 4
 wb.save()
 wb.close()
 return 

