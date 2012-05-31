#!/usr/bin/env python
import sys; 
import os;
import itertools;
import bisect;

pseudoFortunate = {}
admissibleNumbers = {}
primesArr = []
primesLT2pow15 = []
maxPrimeIdx=1000

iMAX=10**9
print "%x"%iMAX
print "%x"%(2**30)

def ReadPrimes():
    global primesArr, primesLT2pow15
    if len(primesArr)>0: return
    f = open('primes1.txt', 'r')
    primesArr = f.read()
    primesArr = map(int, primesArr.split())
    print len(primesArr)
    primesLT2pow15 = [ i for i in primesArr if i < (2**15) ]


def IsPrime(n, debug=0):
    global primesLT2pow15
    for p in primesLT2pow15:
	if p>n/2: return True;
	if n%p == 0: 
	    if debug: print "IsPrime:2:", n, p
	    return False;
    if debug: print "IsPrime:3:", n
    return True;

def FindMaxPrimeIdx():
    global iMAX, maxPrimeIdx
    prod=1.0
    i=0
    while prod < iMAX:
        prod *= primesArr[i]
        print primesArr[i], i, iMAX, prod
        i+=1
    print i
    maxPrimeIdx = i
    return i


def bfs_calc(primes, ppows_arg, idx):
    global iMAX, admissibleNumbers
    retVal = False
    ppows = list(ppows_arg)
    prod = reduce(lambda x,y: x*y, itertools.imap(pow, primes, ppows_arg), 1)
    retVal = (prod < iMAX)
    if retVal:
	admissibleNumbers[prod] = (prod, primes[-1], len(primes))
    print retVal, prod, iMAX, idx, ppows_arg, primes
    if idx >= len(ppows_arg): return retVal 
    # descendant loop
    while retVal == True: 
	# incr this idx, re-calc desc
	retValDesc = bfs_calc(primes, ppows, idx+1)
	if retValDesc == False:
	    print "Desc:", retValDesc, idx, ppows, primes
	    break
	ppows[idx] += 1
    return retVal


def FindAdmissibleNums():
    global maxPrimeIdx, primesArr
    for j in range(1,maxPrimeIdx+1):
        subset_q = [ primesArr[i] for i in range(0,j)]
        print "SUBSET:", subset_q
        powvals = [ 1 for i in subset_q ]
        powvals0 = list(powvals) 
        bfs_calc(subset_q, powvals0, idx=0)


def doPrep():
    ReadPrimes();
    maxPrimeIdx=FindMaxPrimeIdx()


### main 
doPrep();
print len(primesLT2pow15)
for p in primesLT2pow15:
    print p

FindAdmissibleNums();


kadm = admissibleNumbers.keys()
kadm.sort()
print len(kadm), kadm
num = 0
sum = 0
for k in kadm:
    i = admissibleNumbers[k]
    idx_ = bisect.bisect_left(primesArr, i[0]+2)
    if idx_+1 < len(primesArr):
        print i[1], primesArr[i[2]], IsPrime(i[0]+primesArr[i[2]]), i[0], primesArr[idx_]
        num += 1
	pseudoFortunate[ (primesArr[idx_]-i[0]) ] = 1
    else:
	foundM = False;
	for p in range(3, 1001, 2):
	    if IsPrime(i[0]+p, 1):
		print i[1], primesArr[i[2]], i[0], i[0]+p, "--"
                pseudoFortunate[p] = 1
		foundM = True
		break;
        if not foundM:
	    print i[1], primesArr[i[2]], i[0], "---"

print num

kpf = pseudoFortunate.keys()
sum = 0
for i in kpf:
    sum += i
print kpf, reduce(lambda x,y:x+y, kpf, 0), sum

exit(0)
