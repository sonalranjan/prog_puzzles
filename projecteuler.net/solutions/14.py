#!/usr/bin/env python
import sys; 
import os;

# collatz chain
cchain = []
chainLengths = {}

def CollatzChain(n):
    global cchain
    cchain.append(n)
    if n==1: return
    if n%2==0:
	n = n/2
    else:
	n = 3*n+1
    CollatzChain(n)

#(startn, endn) = (999999, 900000)
(startn, endn) = (899999, 800000)
#(startn, endn) = (799999, 700000)

for i in range(startn, endn, -1):
    CollatzChain(i)
    l = len(cchain)
    cchain = []
    if l in chainLengths.keys():
	chainLengths[l].append(i)
    else:
	chainLengths[l] = [i]

k = chainLengths.keys()
k.sort()
print k[-1], chainLengths[k[-1]]
