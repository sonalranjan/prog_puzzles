#!/usr/bin/env python
import sys; 
import os;

f = open('pe_11.txt', 'r')
m = []

for l in f:
    m.append( map(int, l.split()))

print len(m)
print m

tot_prodr = 0

lim = 20
span = 4
for i in range(0, lim):
    for j in range(0, lim-span+1):
	p = [ (i,j+k) for k in range(0, span)] 
	print p 
	prodr = reduce(lambda x,y: x*m[i][j+y], range(0,span), 1)
	if prodr > tot_prodr:
	    tot_prodr = prodr
	    p = [ m[i][j+k] for k in range(0, span)]
	    print tot_prodr, "row: ", (i,j), p, reduce(lambda x,y:x*y, p, 1)
    print "********"

for i in range(0, lim-span+1):
    for j in range(0, lim):
	p = [ (i+k,j) for k in range(0, span)] 
	print p 
	prodr = reduce(lambda x,y: x*m[i+y][j], range(0,span), 1)
	if prodr > tot_prodr:
	    tot_prodr = prodr
	    p = [ m[i+k][j] for k in range(0, span)]
	    print tot_prodr, "col: ", (i,j), p, reduce(lambda x,y:x*y, p, 1)
    print "********"


############################################################
# pick a start: s=(i,j) see if e=(i+4,j+4) is still within matrix bounds
############################################################
for i in range(0, lim-span+1):
    for j in range(0, lim-span+1):
	prodr = reduce(lambda x,y: x*m[i+y][j+y], range(0,span), 1)
	p = [ (i+k,j+k) for k in range(0, span)]
	print p, prodr
        if prodr > tot_prodr:
	    tot_prodr = prodr
            p = [ m[i+k][j+k] for k in range(0, span)]
	    print tot_prodr, "diag: ", (i,j), p, reduce(lambda x,y:x*y, p, 1)

print tot_prodr
