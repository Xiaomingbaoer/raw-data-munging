# Place code below to do the analysis part of the assignment.
import csv

def ave(a):
    result=0
    for i in a:
        result+=float(i)
    return format(result/10, ".2f")

csvfile=open('clean_data.csv',newline='')
tempreader=csv.reader(csvfile,delimiter=',',quotechar='|')
JD=[]
lastyear=0
for row in tempreader:
    #print(row)
    JD.append(row[13])
    if row[0]=="2021":
        #print(row)
        for i in row[1:9]:
           lastyear+=float(i)

newJD=JD[1:-2]
lasttwoline=JD[-2:]
#print(lasttwoline)
allmean=[]
for i in range(0,140,10):
    lst=[]
    a=0
    while a<10:
        lst.append(newJD[i+a])
        a+=1
    allmean.append(ave(lst))

lasttwoyears=(lastyear+float(lasttwoline[0])*12)/20
allmean.append(format(lasttwoyears,".2f"))
print(allmean)