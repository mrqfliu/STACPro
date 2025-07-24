"""this is an example to run on 27.18.114.42"""
"""note: the protein IDs should not contain '(' or ')'"""
"""this scrip is to be submitted in parallel to compute the similarity between all proteins"""
import sys
import get_alignments
import pandas as pd
######### this are parameters to be modified
pdb_folder_path=sys.argv[1]
usalign_path='/share/org/BGI/bgi_wangdt/liuqifan/USalign/USalign'
# this inputs depend on the output of step 1
sublist_path = sys.argv[2]
pdb_list_path = sys.argv[3]
# par_num should be the same as in step1
par_num = sys.argv[4]

######### this lines you do not need to touch
pdb_list = pd.read_csv(pdb_list_path, sep='\t', header=None)
parallel = 1
# use for loop over "par_index" to submit the computation in parallel, with par_index = 0 ~ par_num
align_all_path = get_alignments.compute_similarity(pdb_folder_path, usalign_path, parallel=parallel,
                                                   par_index=int(sys.argv[5]), par_num=par_num, pdb_list=pdb_list, sublist_path=sublist_path)
print('Please use this path as the "align_folder_path" input for the next step:')
print(align_all_path)
