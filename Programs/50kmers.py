#!/usr/bin/env python3
# 50kmers.py

import sys

# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
#    2. The size of k

# set size of k
k = int(sys.argv[2])

# kmer array
kmers = []
# counts array 
counts = [0] * 4**k

# open file
with open(sys.argv[1]) as file:
	
	# define sequence as file after 1st '>' line to end
	lines = file.readlines()
	# remove '\n' character from lines
	for i in range(len(lines)):
		lines[i] = lines[i].replace('\n','')
	sequence = ''.join(lines[1:])
	
	# for each kmer of size k
	for i in range(len(sequence)-(k-1)):
		kmer = sequence[i:i+k]
		
		# check array if already found
		# if found, add the count of that kmer by 1
		# else, add kmer to the array and increase count to 1 
		if kmer not in kmers: 
			kmers.append(kmer)
		# sort kmers alphabetically
		kmers.sort()
		# add count for each occurrence of kmer in sequence
		counts[kmers.index(kmer)] += 1
# print output
for i in range(len(kmers)):
	print(f'{kmers[i]:<3} {counts[i]:<7} {counts[i]/len(sequence):.4f}')


	
	
	
"""
python3 50kmers.py ../Data/chr1.fa 2
AA	33657	0.1106
AC	15836	0.0520
AG	18244	0.0600
AT	27223	0.0895
CA	18965	0.0623
CC	10517	0.0346
CG	8147	0.0268
CT	18142	0.0596
GA	19994	0.0657
GC	9673	0.0318
GG	10948	0.0360
GT	16348	0.0537
TA	22344	0.0734
TC	19744	0.0649
TG	19624	0.0645
TT	34869	0.1146
"""
