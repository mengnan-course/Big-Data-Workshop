# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 22:46:12 2015

@author: Monaen
"""


import openpyxl as px
#import numpy as np


def NationParse(nation, region, count = 0):
    parsenation = []
    parseregion = []
    Count = []
    for i in xrange(len(nation)):
        if len(parsenation) == 0:
            parsenation.append(nation[0])
            parseregion.append(region[0])
        elif parsenation[-1] != nation[i]:
            parsenation.append(nation[i])
            parseregion.append(region[i])
            Count.append(count)
            count = 0
        count += 1
    Count.append(count)
    return parsenation, parseregion, Count



def ItemParse(item, Count):
    parseitem = [];
    temp = [];
    for i in xrange(len(Count)):
        for j in xrange(Count[i]):
            if i == 0:
                temp.append(item[Count[i]+j-1])
            elif i>0:
                temp.append(item[sum(Count[0:i])+j])
        parseitem.append(temp)
        temp = [];
    
    return parseitem
    
    
    
    
    
    
    
    
    
    
    
parent_Path = 'M:\GithubCourse\Big-Data-Workshop'

W = px.load_workbook('raw_data.xlsx', use_iterators = True)
p = W.get_sheet_by_name(name = 'Sheet1')

a = []

Nation = [];nation = []
NationCount = []
Region = []; region = []
Year = []; year = []
Property1 = []; pro1 = []
Property2 = []; pro2 = []
Property3 = []; pro3 = []
flage = 0;
for row in p.iter_rows():
    if len(row)!=6:
        raise Exception('The format of data (Nation,Year,Property1,Property2, Property3) is wrong...')
    for k in row:
        a.append(k.internal_value)
    nation.append(a[0])
    region.append(a[1])
    year.append(a[2])
    pro1.append(a[3])
    pro2.append(a[4])
    pro3.append(a[5])
    a = []
    


Nation, Region, NationCount = NationParse(nation, region)
Year = ItemParse(year, NationCount)
Property1 = ItemParse(pro1, NationCount)
Property2 = ItemParse(pro2, NationCount)
Property3 = ItemParse(pro3, NationCount)


Num = len(Nation)

## Output json file

json = open("nations2.json", "w+")
json.write("[\n\t")
for i in xrange(Num-1):
    json.write('{\n\t\t"name":"' + Nation[i+1] + '",\n\t\t')
    json.write('"region":"'+ Region[i+1] + '",\n\t\t')
    
    
    ## Write [Year, Property1]
    json.write('"' + Property1[0][0] + '":[')
    for j in xrange(len(Property1[i+1])):
        if Property1[i+1][j] == None:
            continue
        json.write('[' + str(int(Year[i+1][j])) + ',' + str(Property1[i+1][j]) + ']')
        if j != len(Property1[i+1])-1:
            if j == len(Property1[i+1])-2 and Property1[i+1][j+1] == None:
                continue
            else:
                json.write(',')
        #elif j == len(Property1[i+1])-1:
            #json.write('[' + str(int(Year[i+1][j])) + ',' + str(Property1[i+1][j]) + ']')
    json.write('],\n\t\t') 
        
    ## Write [Year, Property2]
    json.write('"' + Property2[0][0] + '":[')
    for j in xrange(len(Property2[i+1])):
        if Property2[i+1][j] == None:
            continue
        json.write('[' + str(int(Year[i+1][j])) + ',' + str(Property2[i+1][j]) + ']')
        if j != len(Property2[i+1])-1:
            if j == len(Property2[i+1])-2 and Property2[i+1][j+1] == None:
                continue
            else:
                json.write(',')
        #elif j == len(Property2[i+1])-1:
            #json.write('[' + str(int(Year[i+1][j])) + ',' + str(Property2[i+1][j]) + ']')
    json.write('],\n\t\t') 


    ## Write [Year, Property3]
    json.write('"' + Property3[0][0] + '":[')
    for j in xrange(len(Property3[i+1])):
        if Property3[i+1][j] == None:
            continue
        json.write('[' + str(int(Year[i+1][j])) + ',' + str(Property3[i+1][j]) + ']')
        if j != len(Property3[i+1])-1:
            if j == len(Property3[i+1])-2 and Property3[i+1][j+1] == None:
                continue
            else:
                json.write(',')
        #elif j == len(Property3[i+1])-1:
            #json.write('[' + str(int(Year[i+1][j])) + ',' + str(Property3[i+1][j]) + ']')
    json.write(']\n\t\t') 

    if i+1 != Num-1:
        json.write('},\n\n\n\t')        

json.write('}\n]')
json.close()






