"""
Given an integer, , print its first  multiples. 
Each multiple  (where ) should be printed on 
a new line in the form: n x i = result.
"""

import sys

print "type a number"
n = int(raw_input().strip())

for integer in range(1, 11):
    print n, "x", integer, "=", (n*integer)
