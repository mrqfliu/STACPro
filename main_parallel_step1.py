"""this is an example to run on192.168.66.203"""
"""note: the protein IDs should not contain '(' or ')'"""
import os
import get_lists
import sys
######### this are parameters to be modified
pdb_folder_path = sys.argv[1]
# define how many jobs you want to divide the alignment computation into.
par_num = int(sys.argv[2])

######### this lines you do not need to touch
parallel = 1
pdb_list, pdb_list_path = get_lists.get_lists(pdb_folder_path, parallel=parallel, par_num=par_num)
print('Please use this path as the "sublist_path" input for the next step:')
print(pdb_list_path)
prjfoler = os.path.dirname(pdb_folder_path)
pdb_txt_path = os.path.join(prjfoler, 'pdb_list.txt')
print('Please use this path as the "pdb_list_path" input for step2 and step3:')
print(pdb_txt_path)