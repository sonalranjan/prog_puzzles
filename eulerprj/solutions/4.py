#!/usr/bin/env python
import sys; 
import os;

def IsPalindrome(n):
    s = str(n)
    print s
    l = len(s)
    for i in range(0, (l/2)+1):
	diffS = ord(s[i])-ord(s[l-1-i]);
	if not diffS == 0:
	    print s[i], s[l-1-i], diffS
	    return False
    return True

for i in range(999, 99, -1):
    for j in range(i-1, 99, -1):
	num = i*j
	print num, i, j
	if IsPalindrome(num):
	    print "PALINDROME: ", num, i, j
