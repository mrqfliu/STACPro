"""this is an example to run on 192.168.66.203"""
"""note: the protein IDs should not contain '(' or ')'"""
import get_lists
import get_alignments
import clustering.get_clusters
pdb_folder_path = '/share/org/BGI/bgi_wangdt/RoseTTAFold/rosetta/0803'
usalign_path = '/share/org/BGI/bgi_wangdt/liuqifan/USalign/USalign'
pdb_list, pdb_list_path = get_lists.get_lists(pdb_folder_path)
align_all_path = get_alignments.compute_similarity(pdb_folder_path, usalign_path)
clustering.get_clusters.get_tree_file(align_all_path, plot=1)
