#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

genome_size = int(sys.argv[1])
read_number = int(sys.argv[2])
read_length = int(sys.argv[3])

# set size of chromosome array containing data

chromosome = [0] * genome_size
coverage_sum = 0


for i in range(read_number):
	# simulate random sequence of length 100 to sequence 
	lower_bound = random.randint(0, genome_size - (read_length + 1))
	upper_bound = lower_bound + read_length - 1
	
	# sequence each nucleotide in 100 bp window
	for x in range (lower_bound, upper_bound):
		chromosome[x] += 1
chromosome.sort()

print(chromosome)
# print coverages
coverage_sum = sum(chromosome[read_length:])

print(f'Minimum: {chromosome[i]} Maximum: {chromosome[-1]} Average: {coverage_sum/len(chromosome[read_length:]):.5f}')



"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
