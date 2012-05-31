#!/usr/bin/env python
import sys; 
import os;
import itertools;
import bisect;

primesArr = []

iMAX=10**9
print "%x"%iMAX
print "%x"%(2**30)

def ReadPrimes():
    global primesArr
    if len(primesArr)>0: return
    f = open('primes1.txt', 'r')
    primesArr = f.read()
    primesArr = map(int, primesArr.split())
    print len(primesArr)


def doPrep():
    ReadPrimes();


### main 
doPrep();

sum = 0
for p in primesArr:
    if p > 2000000: break
    sum += p

print sum

exit(0)
