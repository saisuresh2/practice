#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'

anti = ""
i = len(dna)-1
while (i >= 0):
	for nt in dna[i]:
		if (nt == "A"): anti += anti.join("T")
		elif (nt == "T"): anti += anti.join("A")
		elif (nt == "C"): anti += anti.join("G")
		elif (nt == "G"): anti += anti.join("C")
	i = i - 1
print(anti)

"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
