#!/usr/bin/env python
import sys; 
import os;

max = 4*(10**6);
max = 10**1000;
### max = 100 

fib2 = [1, 2]
step = 2
sum = 2
i = fib2[0] + fib2[1]
print i

while i < max:
    step += 1 
    if (i%2==0): 
	sum += i
    fib2.append(i)
    fib2.pop(0)
    print fib2
    i = fib2[0] + fib2[1]
    print i, len(str(i)), step

print sum
