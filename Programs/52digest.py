#!/usr/bin/env python3
# 52digest.py

import re
import sys

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments

# read in restriction pattern argument
restr_pattern = sys.argv[2]
# open genome file
with open(sys.argv[1]) as genome_file:
	
	# read file
	lines = genome_file.readlines()

	# extract genome sequence 
	for i in range(len(lines)):
		lines[i] = lines[i].replace('\n','')
		if re.search("ORIGIN", lines[i]): 
			seq_start = i+1
		if re.search("//", lines[i]):
			seq_end = i-1
	# extract sequence, join it, and reformat
	sequence = lines[seq_start:seq_end]
	sequence = ''.join(sequence)
	sequence = sequence.replace(' ' , '')
	# remove digits
	sequence = re.sub('\d+', '', sequence)
	
# look for restriction pattern in file

restr_indexes = []

for match in re.finditer(restr_pattern, sequence):
	# save start and ending positions of pattern found
	restr_indexes.append(match.start())
	restr_indexes.append(match.end())

for i in range(len(restr_indexes)-1):
	# first fragment is beginning of sequence to first match
	if i == 0: 
		frag = sequence[0:restr_indexes[i]]
	# other fragments are starting of last match to beginning of next match
	elif (i % 2) != 0:
		frag = sequence[restr_indexes[i-1]:restr_indexes[i+1]]
	# if index not corresponding to a match.end(), go to next i 
	else:
		continue
	# print length of digested fragments
	print(len(frag))
"""
python3 52digest.py ../Data/sars-cov2.gb gaattc
1160
10573
5546
448
2550
2592
3569
2112
1069
"""
