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

def addmy(a,b):
    global lim
    return ((a+b)%lim)


print "ROW"
for i in range(0, lim):
    for j in range(0, lim):
	### p = [ (i,addmy(j,k)) for k in range(0, span)]  
	### print p  
	prodr = reduce(lambda x,y: x*m[i][addmy(j,y)], range(0,span), 1)
	if prodr > tot_prodr:
	    tot_prodr = prodr
	    p = [ m[i][addmy(j,k)] for k in range(0, span)]
	    print tot_prodr, "row: ", (i,j), p, reduce(lambda x,y:x*y, p, 1)
    print "********"

print "COL"
for i in range(0, lim):
    for j in range(0, lim):
	### p = [ (addmy(i,k),j) for k in range(0, span)]  
	### print p  
	prodr = reduce(lambda x,y: x*m[addmy(i,y)][j], range(0,span), 1)
	if prodr > tot_prodr:
	    tot_prodr = prodr
	    p = [ m[addmy(i,k)][j] for k in range(0, span)]
	    print tot_prodr, "col: ", (i,j), p, reduce(lambda x,y:x*y, p, 1)
    print "********"


print "DIAG"
for i in range(0, lim):
    for j in range(0, lim):
	prodr = reduce(lambda x,y: x*m[addmy(i,y)][addmy(j,y)], range(0,span), 1)
	### p = [ (addmy(i,k),addmy(j,k)) for k in range(0, span)] 
	### print p, prodr 
        if prodr > tot_prodr:
	    tot_prodr = prodr
            p = [ m[addmy(i,k)][addmy(j,k)] for k in range(0, span)]
	    print tot_prodr, "diag: ", (i,j), p, reduce(lambda x,y:x*y, p, 1)

print "ANTIDIAG"
for i in range(0, lim):
    for j in range(0, lim):
	prodr = reduce(lambda x,y: x*m[addmy(i,y)][addmy(j,-y)], range(0,span), 1)
	### p = [ (addmy(i,k),addmy(j,-k)) for k in range(0, span)] 
	### print p, prodr 
        if prodr > tot_prodr:
	    tot_prodr = prodr
            p = [ m[addmy(i,k)][addmy(j,-k)] for k in range(0, span)]
	    print tot_prodr, "antidiag: ", (i,j), p, reduce(lambda x,y:x*y, p, 1)

print tot_prodr
