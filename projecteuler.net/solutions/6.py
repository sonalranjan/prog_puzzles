#!/usr/bin/env python
import sys; 
import os;

sum = 0
for i in range(1, 101):
    for j in range(i+1, 101):
        sum += (2*i*j)

print sum
