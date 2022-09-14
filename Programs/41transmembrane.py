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
hydropathy_scores = [4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, 
	-0.9, -1.3, -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5]

def kd_calc(peptide):
	sum = 0
	for i in range(0, len(peptide)):
		for j in range(0, len(amino_acids)):
			if (peptide[i] == amino_acids[j]):
				#print("kd_calc: ", peptide, amino_acids[j], hydropathy_scores[j])
				sum += hydropathy_scores[j]
				
	#print(KD)
	KD = sum/len(peptide)
	return (KD)

#print(kd_calc("IVLIVLIVLIVAAAAAAA"))

def amphipathic_a_helix(protein):
	first_30aa = protein[:30]
	after_30aa = protein[30:]
	search = False
	sp = False
	hydro = False
	# test signal peptides of len 8 by calculating KD
	for i in range(0, len(first_30aa),8):
		signal_peptide = first_30aa[i:i+8]
		if (len(signal_peptide) == 8):
			sp_kd = kd_calc(signal_peptide)
		if (sp_kd > 2.5):
			#print('found sp! ', signal_peptide)
			sp = True
			break
		else: sp = False
	# check for hydrophobic regions in same protein
	for j in range(0,len(after_30aa),11):
		hydrophobic_peptide = after_30aa[i:i+11]
		if ( (len(hydrophobic_peptide) == 11) and 'P' not in hydrophobic_peptide):
			hyd_kd = kd_calc(hydrophobic_peptide)
			if (hyd_kd > 2.0):
				#print('found hydrophobic! ',hydrophobic_peptide)
				hydro = True
				break
			else: hydro = False
	print(sp, hydro)
	if (sp==True or hydro==True):
		return True
		print('amphipathic!')
	else:
		return False


# read in proteins from file

with open(sys.argv[1]) as fp:
	lines = fp.readlines()
	
	for i in range(len(lines)):
		if lines[i].startswith('>'):
			protein_name = lines[i]
			protein_name = protein_name[0:protein_name.index(' ')]
			protein_name = protein_name.replace('>','')
			protein_start = i + 1
		if lines[i].endswith('*\n'):
			protein_end = i
			fullprotein = ''.join(lines[protein_start:protein_end + 1])
			fullprotein = fullprotein.replace('*\n','')
			fullprotein = fullprotein.replace('\n','')
			if (amphipathic_a_helix(fullprotein)):
				print(protein_name)

"""
python3 40transmembrane.py ../Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
