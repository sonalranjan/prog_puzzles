#!/usr/bin/env python
import sys; 
import os;

f = open('names_22.txt', 'r')
n = f.read()
n = n.split(',');


def name_val1(nam):
    sum = 0
    for i in range(1, len(nam)-1):
	sum += (ord(nam[i])-ord('A')+1);
	### print nam[i],sum 
    return sum

def name_val(nam):
    return reduce(lambda x,y: x+ord(nam[y])-ord('A')+1, range(1, len(nam)-1), 0) 

print len(n), n[0]
n.sort()
sum = 0
for i in range(0, len(n)):
    print i, name_val(n[i]), n[i]
    sum += (i+1)*name_val(n[i])
print sum

print name_val("CAB") 

