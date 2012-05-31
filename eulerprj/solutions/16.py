#!/usr/bin/env python
import sys; 
import os;

print reduce(lambda x,y:int(x)+int(y), str(2**1000), 0)
