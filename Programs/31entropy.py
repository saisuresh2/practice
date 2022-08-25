#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys

p = []
for i in range(len(sys.argv)-1):
	p.append(float(sys.argv[i+1])) 
p.sort()

# Calculation
H = 0
for prob in p:
	H -= (prob * (math.log(prob, 2)))

print(H)
"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
