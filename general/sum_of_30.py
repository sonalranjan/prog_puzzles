#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import itertools

allowed_numbers = [ k for k in range(1,16, 2)]
LOOKUP_DICT = dict([(k, int(k)) for k in '0123456789'])

def fill_pair(s, k):
  tbd = s - k
  skdiff_pairs = []
  for n in allowed_numbers:
    if (tbd - n) in allowed_numbers:
      skdiff_pairs += [ (n, tbd - n) ]
  return skdiff_pairs

def num_base(n, b):
  b = int(b)
  for k in str(n):
    if LOOKUP_DICT[k] >= b:
      return -1
  return sum([ LOOKUP_DICT[k]*(b**idx) for (idx, k) in
              enumerate(str(n)[::-1]) ])

def interesting_num_base():
  for k in allowed_numbers:
    for b in allowed_numbers:
      nb = num_base(k, b)
      if nb == -1: continue
      yield k, b, nb



def main(argv):
  # print allowed_numbers
  # print fill_pair(30, 12)
  # for n in argv: print n, num_base(n, 12)
  for t in interesting_num_base():
    #  print t
    l = [ (t[0], t[1][0], t[1][1]) for t in itertools.product(["(%s)%s=%s"%t], fill_pair(30, t[-1])) ]
    if len(l): print l



if __name__ == '__main__':
  main(sys.argv[1:])
