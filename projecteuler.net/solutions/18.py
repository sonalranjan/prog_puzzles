#!/usr/bin/env python
import sys; 
import os;
import numpy;
from scipy import sparse;

f = open('pe_18.txt', 'r')
m = []

for l in f:
    m.append( map(int, l.split()))

k = len(m[-1])
print len(m)
print m[-1], k

mat = numpy.zeros(shape=(3,3))
print mat
print mat[1,1]

mat_s = sparse.lil_matrix((k,k))
for r in range(0, len(m)):
    for c in range(0, len(m[r])):
	mat_s[r, c] = m[r][c]



print mat_s.rows
print mat_s.data

exit(0)

for r in mat_s.rows:
    print r

