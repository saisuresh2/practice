#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
# Hints:
#   Create a function for KD calculation
#   Create a function for amphipathic alpha-helix
amino_acids = ["I", "V", "L", "F", "C", "M", "A", "G", "T", "S", "W", "Y",
				"P", "H", "E", "Q", "D", "N", "K", "R"]
hydropathy_scores = [4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.9,
						-1.3, -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5]
def kd_calc(alpha_helix):
	KD = 0
	#print(len(protein))
	for i in range(0, len(protein)):
		for j in range(len(amino_acids)):
			if (protein[i] == amino_acids[j]):
				KD += hydropathy_scores[j]
				#print(amino_acids[j], hydropathy_scores[j])
	#print(KD)
	KD = KD/len(protein)
	return (KD)

#print(kd_calc("IVLIVLIVLIVAAAAAAA"))

def amphipathic_a_helix(protein):
	
"""
python3 40transmembrane.py ../Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
