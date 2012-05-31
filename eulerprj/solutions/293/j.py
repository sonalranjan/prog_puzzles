#!/usr/bin/env python
import sys; 
import os;
import itertools;

iMAX=10**9
print "%x"%iMAX
print "%x"%(2**30)

f = open('primes1.txt', 'r')
q = f.read()
q = q.split()
print len(q)

prod=1.0
i=0
while prod < iMAX:
    prod *= float(q[i])
    print q[i], i, iMAX, prod
    i+=1

print i
maxPrime=i

maxPow=[ [] for i in range(0, maxPrime+1) ]
for j in range(0,maxPrime+1):
    maxPow[j]=range(1,31)

for j in range(1,maxPrime+1):
    subset_q = [ int(q[i]) for i in range(0,j)]
    print "SUBSET:", subset_q
    powvals = [ 1 for i in subset_q ]
    powvals0 = list(powvals) 
    for powidx in range(0, j):
	for powval in range(0, 30):
	    powvals1 = powvals0
	    powvals1[powidx]+=1
            print "POWVALS", powvals1
            pairs_qp = zip(subset_q, powvals1)
	    prod=1.0
            zl = [ p[0]**p[1] for p in pairs_qp ]
	    print "ZL", zl
	    prod = reduce(lambda x,y: x*y, zl, 1.0)
	    if prod > iMAX: break
	    print "PROD:", prod
        if powvals0[powidx]
        powvals0[powidx]
	


