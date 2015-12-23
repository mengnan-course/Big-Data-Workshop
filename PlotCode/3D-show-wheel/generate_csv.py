import openpyxl as px
#import numpy as np


W = px.load_workbook('raw_data.xlsx', use_iterators = True)
p = W.get_sheet_by_name(name = 'Sheet1')

#Year = []; year = []
#English = [];
#French = [];
#Spanish = [];
#Russian = [];
#German = [];
#Chinese = [];
#Hebrew = [];
#total = [];


a = []
flage = 0;
for row in p.iter_rows():
    if flage == 0:
        b = [[]]*len(row)
        for item in xrange(len(b)):
            b[item] = []   # decorrelation
        flage += 1
    for k in xrange(len(row)):
        a.append(row[k].internal_value)
    
    for j in xrange(len(row)):
        b[j].append(a[j])
    a = []


year = b[0][1:]

for i in xrange(len(b[0])-1):
    b[0][i+1] = int(year[i])






csv = open("data_generated.csv", "w+")
csv.write('symbol,date,price\n')
symbol=2
#for symbol in xrange(len(b)-1): # no year
for num in xrange(len(b[symbol+1])-1):
    csv.write(b[symbol+1][0])
    csv.write(',Dec ')
    csv.write(str(b[0][num+1]))
    csv.write(',')
    csv.write(str(b[symbol+1][num+1]))
    csv.write('\n')





symbol=1
#for symbol in xrange(len(b)-1): # no year
for num in xrange(len(b[symbol+1])-1):
    csv.write(b[symbol+1][0])
    csv.write(',Dec ')
    csv.write(str(b[0][num+1]))
    csv.write(',')
    csv.write(str(b[symbol+1][num+1]))
    csv.write('\n')


    
symbol=3
#for symbol in xrange(len(b)-1): # no year
for num in xrange(len(b[symbol+1])-1):
    csv.write(b[symbol+1][0])
    csv.write(',Dec ')
    csv.write(str(b[0][num+1]))
    csv.write(',')
    csv.write(str(b[symbol+1][num+1]))
    csv.write('\n')



symbol=5
#for symbol in xrange(len(b)-1): # no year
for num in xrange(len(b[symbol+1])-1):
    csv.write(b[symbol+1][0])
    csv.write(',Dec ')
    csv.write(str(b[0][num+1]))
    csv.write(',')
    csv.write(str(b[symbol+1][num+1]))
    csv.write('\n')

#symbol=6
##for symbol in xrange(len(b)-1): # no year
#for num in xrange(len(b[symbol+1])-1):
    #csv.write(b[symbol+1][0])
    #csv.write(',Dec ')
    #csv.write(str(b[0][num+1]))
    #csv.write(',')
    #csv.write(str(b[symbol+1][num+1]))
    #csv.write('\n')
    
csv.close()