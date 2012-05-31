#!/usr/bin/env python
import sys; 
import os;

def max_primepow(n, p):
    """
    returns [residue_n, pow_of_p]
    where: 
    * pow_of_p is the largest power of p in n
    * residue_n = n/(p^pow_of_p)
    """
    if 0!=n%p:
	return [n, 0]
    powp = p
    pow_p = 1
    while 0==n%p:
	n = n/p
	pow_p += 1
    return [n, pow_p-1]

def prime_factorization(n):
    prime_factors = []
    res_n = n
    lim = int(res_n**(0.5)+1)
    i = 2
    while i < lim:
	### print "i=%d lim=%d"%(i,lim) 
	[res_n, powi] = max_primepow(res_n, i)
	if 0!=powi:
	    ### print "prime (%d,%d) divs %d"%(i,powi,(res_n*(i**powi))) 
	    lim = int(res_n**(0.5)+1)
	    ### print "i=%d lim=%d res_n=%d"%(i,lim,res_n) 
	    prime_factors.append((i, powi))
        i+=1
    if res_n > 1:
	prime_factors.append((res_n, 1))
    return prime_factors

def euler_totient(n):
    pf = prime_factorization(n)
    prod = 1
    for pfelem in pf:
	prod *= (pfelem[0]-1)*(pfelem[0]**(pfelem[1]-1))
    return prod

#************************************
#
#************************************

if __name__ == "__main__":
    num = 36
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    print prime_factorization(num)
    print euler_totient(num)

