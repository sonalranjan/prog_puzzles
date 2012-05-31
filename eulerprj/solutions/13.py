#!/usr/bin/env python
import sys; 
import os;

sum = 0
f = open('pe_13.txt','r')
for i in f:
    sum += int(i)

print sum
