#!/usr/bin/env python
import sys; 
import os;

############################################################
# Any achilles number has to be of the form:
# n = prod(prime(i)^pow(i)) 
# where: 
#  1. i >= 2 [ otherwise, it has to be "perfect number" too ] 
#  2. pow(i) >= 2 [ since prime(i)^2 should divide n ]
#  3. gcd(pow(i)) = 1 [ otherwise, n can be represented as m^k, where k = gcd(pow(i)) ]
#
############################################################



############################################################
# plan of action:
#  1. some how generate sets of numbers that have gcd = 1
#  2. recursive algo to find largest prime needed to be considered 
############################################################


