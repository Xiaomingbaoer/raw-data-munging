# Place code below to do the munging part of this assignment.
rawdata=open('data.txt','r').readlines()[8:]
heading=open('data.txt','r').readlines()[7]
heading=','.join(heading.split()[:-1])+'\n'
cleandata=[]
cleandata.append(heading)
#print(heading)
for line in rawdata:
    if line[0].isnumeric():
        newline=line.split()
        year=newline[0:1]  #year column 
        newline_no_year=newline[1:]#the others
        for i in newline_no_year:
            if i=='***':
               newline_no_year[newline_no_year.index('***')]='NaN'
            elif i=='****':
                newline_no_year[newline_no_year.index('****')]='NaN'
            else:
                a=newline_no_year.index(i)
                newline_no_year[a]=format(float(newline_no_year[a])*0.018,".1f")#C -> F
        year+=newline_no_year
        year_new=year[:-1]
        year_new.append('\n')
        newyear=','.join(year_new)
        cleandata.append(newyear)
newcleandata=''.join(cleandata)

#save the data to csv file
f=open('clean_data.csv','w')
f.write(newcleandata)
f.close()