#!/usr/bin/env python
import sys; 
import os;

def fact(n):
    return reduce(lambda x,y:x*y, range(1, n+1), 1)


print fact(6)
print fact(4)
print (fact(40)/ (fact(20)**2))

