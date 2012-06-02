#!/usr/bin/env python
import sys; 
import os;
import itertools;
import bisect;

primesArr = []
primesLTN = []
Num = 600851475143
N = (600851475143**(0.5))

iMAX=10**9
print "%x"%iMAX
print "%x"%(2**30)

def ReadPrimes():
    global primesArr, primesLTN
    if len(primesArr)>0: return
    f = open('primes1.txt', 'r')
    primesArr = f.read()
    primesArr = map(int, primesArr.split())
    print len(primesArr)
    primesLTN = [ i for i in primesArr if i < N ]


def doPrep():
    ReadPrimes();


### main 
doPrep();

print len(primesLTN)

for i in range(len(primesLTN)-1, 0, -1):
    if Num%primesLTN[i] == 0:
	print "Largest:", primesLTN[i], Num/primesLTN[i]
	Num = Num/primesLTN[i]

exit(0)
