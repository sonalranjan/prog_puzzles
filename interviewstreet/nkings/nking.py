#!/usr/bin/env python
# interview street : N-Kings
import sys
import os

mod_num = 1000000007

############################################################
# chess board processing class
############################################################
class Board:
    def __init__(self, n, k_vals, msg=""):
        self.n = n
        self.k_vals = k_vals
        self.k = len(self.k_vals)
        self.msg = msg
        self.validate
        self.num_count = 0
        if self.k == self.n: self.num_count = 1

    def print_num_count(self):
        print self.num_count%mod_num

    def validate(self):
        pass

    def __str__(self):
        return "Board %s: "%self.msg + str(self.n) + " " + str(self.k) + " " + str(self.k_vals)

    # given tmp_k-rows for nxn board, find valid entries for k+1-th row
    def valid_pos_for_k_plus_1(self, tmp_k_vals):
        tmp_k = len(tmp_k_vals)
        if (tmp_k > self.n-1): return []
        if tmp_k == 0: return range(0, self.n) # { 0 .. n-1 }
        candidates = range(0, self.n) # { 0 .. n-1 }
        # exclude all existing columns in tmp_k_vals  UNION { x in { pos[k]-1, pos[k], pos[k]+1 } | for x in { 0, n-1 } }
        excl = range(max(0, tmp_k_vals[-1]-1), min(self.n-1, tmp_k_vals[-1]+1)+1) + tmp_k_vals 
        return [x for x in candidates if not x in excl ]

    def count_valid_boards(self, cur_k_vals=None):
        if cur_k_vals is None: cur_k_vals = self.k_vals
        # for each row r, recursively find valid positions for r
        valid_k_vals = self.valid_pos_for_k_plus_1(cur_k_vals)
        for kval in valid_k_vals:
            ### print self, cur_k_vals + [kval] 
            if len(cur_k_vals) == self.n-1:
                self.num_count += 1
                #print cur_k_vals + [kval]
            else:
                self.count_valid_boards(cur_k_vals + [kval])
            

############################################################
# main processing loop
############################################################

def read_inp_and_process(debug=False):
    # input number of tests
    num_tests = int(raw_input())
    if debug: print num_tests
    # for each test input ...
    for t in xrange(0, num_tests):
        if debug: print "testcase: ", t
        # input N,K pair
        n, k = [ int(x) for x in raw_input().split() ]
        # input K integers
        k_vals = [ int(x) for x in raw_input().split() ]
        # construct the initial board
        b = Board(n, k_vals, str(t))
        if debug: print b
        # recurse and find the all solutions
        b.count_valid_boards()
        # print number of solutions
        b.print_num_count()


if __name__ == "__main__":
    do_debug = False #True
    read_inp_and_process(do_debug)



