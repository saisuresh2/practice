#!/usr/bin/env python3

import random
random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

nt = ["A","C","G","T"]
random_dna = ""

for i in range(30):
	random_dna += random_dna.join(random.choices(nt, weights=(30,20,20,30)))
	
# Calculate AT freq
count = 0
for f in random_dna:
	if (f == "A" or f == "T"):
		count += 1
	else: continue

print(len(random_dna), str(count/len(random_dna)), random_dna)

"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
