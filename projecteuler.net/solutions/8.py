#!/usr/bin/env python
import sys; 
import os;

f = open('pe_8.txt', 'r')

### make one string 

l = ""
for i in f:
    if i.endswith('\n'):
	l += i[:-2]
    else:
	l += i

print l

max_prod = 1

for i in range(0, len(l)-5):
    prod = reduce(lambda x,y: x*int(l[y]), range(i,i+5), 1)
    if prod > max_prod:
	max_prod = prod
    print l[i:i+5], prod, max_prod


print max_prod

