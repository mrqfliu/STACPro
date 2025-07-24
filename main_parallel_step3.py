"""this is an example to run on 27.18.114.42"""
"""note: the protein IDs should not contain '(' or ')'"""
"""this scrip generates the nwk file for tree plot on itol website"""
import pandas as pd
import get_alignments
import sys
######### this are parameters to be modified
# this inputs depend on the output of step 1
pdb_list_path = sys.argv[1]
align_folder_path = sys.argv[2]

######### this lines you do not need to touch
pdb_list = pd.read_csv(pdb_list_path, sep='\t', header=None)
align_all_path = get_alignments.cat_align(pdb_list, align_folder_path=align_folder_path)
print('Please use this path as the "align_all_path" input for the next step:')
print(align_all_path)

