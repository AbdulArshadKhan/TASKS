import xlrd
wb=xlrd.open_workbook('data.xls')
ws=wb.sheet_by_index(0)
print('\n\n')
valid={}
invalid={}
for y in range(7,ws.nrows):
    if '-' in ws.cell_value(y,0):
        name=ws.cell_value(y,0).split('-')[0]
        if name in valid:
            valid[name]=valid[name]+int(ws.cell_value(y,4))
        else:
            valid[name]=int(ws.cell_value(y,4))
    else:
        name=ws.cell_value(y,0)
        if name in invalid:
            invalid[name]=invalid[name]+int(ws.cell_value(y,4))
        else:
            invalid[name]=int(ws.cell_value(y,4))
import xlsxwriter as xw
wb1=xw.Workbook('valid.xlsx')
ws1=wb1.add_worksheet()
ws1.write('A1','Valid Names')
ws1.write('B1','Time in Session')
x=2
for i in valid:
    ws1.write('A{}'.format(x),i)
    ws1.write('B{}'.format(x),valid[i])
    x=x+1
wb1.close()
wb2=xw.Workbook('invalid.xlsx')
ws2=wb2.add_worksheet()
ws2.write('A1','Invalid Names')
ws2.write('B1','Time in Session')
x=2
for i in invalid:
    ws2.write('A{}'.format(x),i)
    ws2.write('B{}'.format(x),invalid[i])
    x=x+1
wb2.close()
wb3=xw.Workbook('attendence.xlsx')
ws3=wb3.add_worksheet()
attendence={}
for i in valid:
    if(valid[i]>=90):
        attendence[i]='P'
    else:
        attendence[i]='A'
for i in invalid:
    if(invalid[i]>=90):
        attendence[i]='P'
    else:
        attendence[i]='A'
ws3.write('A1','Name')
ws3.write('B1','Attendence')
x=2
for i in attendence:
    ws3.write('A{}'.format(x),i)
    ws3.write('B{}'.format(x),attendence[i])
    x=x+1
wb3.close()
