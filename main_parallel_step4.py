import clustering.get_clusters
import sys
"""this is an example to run on 27.18.114.42"""
"""note: the protein IDs should not contain '(' or ')'"""
"""this scrip generates the nwk file for tree plot on itol website"""

# ######## this are parameters to be modified
align_all_path = sys.argv[1]
# this is to define how many node you want to have in one cluster
#node_number_upward = 3

# ######## this lines you do not need to touch
labels, path_tree_folder = clustering.get_clusters.get_tree_file(align_all_path, method='nj')
labels, path_tree_folder = clustering.get_clusters.get_tree_file(align_all_path, method='upgma')
#labels, path_tree_folder = clustering.get_clusters.get_tree_file(align_all_path, tm_score='rmsd', method='upgma')
#labels, path_tree_folder = clustering.get_clusters.get_tree_file(align_all_path, tm_score='rmsd', method='nj')
#df = clustering.get_clusters.clustering_upward(labels, node_number_upward, path_tree_folder)
# you can define the number of points from the top down as well,
# df = clustering.get_clusters.clustering_downward(labels, node_number_downward, path_tree_folder)
