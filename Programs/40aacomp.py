#!/usr/bin/env python3

import sys

# Make a program that reports the amino acid composition in a file of proteins
#aminoacids = [[W,Wcount],C,H,M,Y,Q,F,N,P,T,R,I,D,G,A,K,E,V,L,S]
protein_sequences = []

with open(sys.argv[1]) as fp:
	lines = fp.readlines()

	for i in range(len(lines)):
		# find beginning of protein sequence indicated by '>'
		if lines[i].startswith('>'):
			protein_start = i + 1

		# find end of protein sequence indicated by *\n
		if lines[i].endswith('*\n'):
			protein_end = i

			# once the protein start and end is found, join the protein
			# as one string
			protein = ''.join(lines[protein_start:protein_end + 1])
			# remove star and newline from sequences
			protein = protein.replace('*\n', '')
			protein = protein.replace('\n', '')
			# add protein to list of proteins
			protein_sequences.append(protein)
# with the protein sequences in our protein_sequences array, we can
# calculate our results
print(protein_sequences)
total_aa = 0
amino_acids = ['W', 'C', 'H', 'M', 'Y', 'Q', 'F', 'N', 'P', 'T', 'R', 'I',
				'D', 'G', 'A', 'K', 'E', 'V', 'L', 'S']
amino_count = [0] * 20

# see which amino acid in amino_acids matches to the aa in the protein
# sequence and increment the corresponding index in amino_count by 1
for protein in protein_sequences:
	for aa in protein:
		total_aa += 1
		for i in range(len(amino_acids)):
			if (aa == amino_acids[i]):
				amino_count[i] += 1
				
# print the result of the amino acid, its count, and the frequency
for i in range(len(amino_acids)):
	print(amino_acids[i], amino_count[i], amino_count[i]/total_aa)
	
#"""		
"""
python3 41aacomp.py ../Data/at_prots.fa
W 528 0.012054244098442994
C 801 0.018286836217524315
H 1041 0.023766038080452946
M 1097 0.025044518515136296
Y 1281 0.02924523994338158
Q 1509 0.03445048171316378
F 1842 0.04205287429797726
N 1884 0.04301173462398977
P 2051 0.046824345920277614
T 2153 0.04915300671202228
R 2320 0.05296561800831012
I 2356 0.05378749828774942
D 2573 0.05874160997214739
G 2732 0.06237158120633761
A 2772 0.06328478151682572
K 2910 0.06643532258800967
E 2989 0.06823889320122369
V 3001 0.06851285329437012
L 3950 0.09017853066070042
S 4012 0.09159399114195699
"""

