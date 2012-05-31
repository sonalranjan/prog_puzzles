#!/usr/bin/env python
import sys; 
import os;

prod = reduce(lambda x,y: int(x)*int(y), range(1,101), 1)
print prod
print reduce(lambda x,y:int(x)+int(y), str(prod), 0)
