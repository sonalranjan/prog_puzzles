#!/usr/bin/env python
import sys; 
import os;

def fact(n):
    return reduce(lambda x,y:x*y, range(1, n+1), 1)


print fact(9), 2*fact(9), fact(8)
print (2*fact(9) + 7*fact(8))-10**6
print fact(7), fact(6), fact(5), fact(4), fact(3), fact(2)

k = 10**6 - (2*fact(9)+6*fact(8)+6*fact(7)+2*fact(6)+5*fact(5)+fact(4)+2*fact(3)+2*fact(2))
#          

# 0123456789
# 2 7 8 3 9 1 5 4 6 0
# 2783915460

print k, k/fact(8)

