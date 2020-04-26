#!/usr/bin/env python3

import csv

num_Khan = 0
num_Correy = 0
num_Li = 0
num_Tooley = 0
total = 0
a = 0

with open ('election.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    firstrow =  next(csvfile)
    for row in reader:
        
        total = total + 1
        
        if str(row[2]) == 'Khan':
            num_Khan = num_Khan + 1

        elif str(row[2]) == 'Correy':
            num_Correy = num_Correy + 1

        elif str(row[2]) == 'Li':
            num_Li = num_Li + 1

num_Tooley = total - num_Khan - num_Li - num_Correy

if num_Khan > num_Li and num_Khan > num_Correy and num_Khan > num_Tooley:
    winr_name = 'Khan'
elif num_Correy > num_Li and num_Correy > num_Khan and num_Correy > num_Tooley:
    winr_name = 'Correy'
elif num_Li > num_Khan and num_Li > num_Correy and num_Li > num_Tooley:
    winr_name = 'Li'
else:
    winr_name = "O'Tooley"

print ('Electron Results')
print ('----------------------------------')
print ('Total votes: ' + str(total))
print ('Khan: ' + 'percent: {:.4%}'.format(num_Khan/total) + ' (' + str(num_Khan) + ')')
print ('Correy: ' + 'percent: {:.4%}'.format(num_Correy/total) + ' (' + str(num_Correy) + ')')
print ('Li: ' + 'percent: {:.4%}'.format(num_Li/total) + ' (' + str(num_Li) + ')')
print ("O'Tooley: " + 'percent: {:.4%}'.format(num_Tooley/total) + ' (' + str(num_Tooley) + ')')
print ('----------------------------------')
print ('Winner: ' + str(winr_name))
print ('----------------------------------')