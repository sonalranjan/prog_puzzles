#!/usr/bin/env python
import sys; 
import os;
import itertools;

bit_p = [0, 1, 2, 4, 8, 5, 9, 10]

def IsAdmissible(n):
    ### return not ((n&(n<<1))); 
    return (0 == nim_sum123(n))

def nim_sum(a, b, c):
    return (a^b)^c 

def nim_sum123(n):
    return nim_sum(n, 2*n, 3*n)

max = 2**30
sum = 0
for p in itertools.product(bit_p, repeat=8):
    num = ( p[0]<<28 |
	    p[1]<<24 |
	    p[2]<<20 |
	    p[3]<<16 |
	    p[4]<<12 |
	    p[5]<<8  |
	    p[6]<<4  |
	    p[7] )

    if num==0: continue
    if num>max: break
    if IsAdmissible(num):
	### print "%s %x %d"%(p, num, num)  
        sum += 1

print sum

exit(0)
