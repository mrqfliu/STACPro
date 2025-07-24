#!/bin/bash
source /share/apps/anaconda3/bin/activate /share/org/BGI/bgi_wangdt/.conda/envs/stacpro

path_structure_folder=$1
parallel_num=$2

path_scripts=/share/org/BGI/bgi_wangdt/liuqifan/stacpro/stacpro-main
path_dir_structure_folder=$(dirname "$path_structure_folder")

### step1
python $path_scripts/main_parallel_step1.py "$path_structure_folder" "$parallel_num"

path_sublist="$path_dir_structure_folder/sublists"
path_pdblist="$path_dir_structure_folder/pdb_list.txt"
path_alignfolder="$path_dir_structure_folder/alignments"
path_align_all="$path_alignfolder/alignment_all.txt"

### step2
mkdir -p "$path_alignfolder"
for ((ind = 0; ind < $parallel_num; ind++))
do
	python "$path_scripts/main_parallel_step2.py" "$path_structure_folder" "$path_sublist" "$path_pdblist" "$parallel_num" "$ind" &
done
wait

### step3
echo "$path_pdblist"
echo "$path_alignfolder"
python "$path_scripts/main_parallel_step3.py" "$path_pdblist" "$path_alignfolder"

### step4
python "$path_scripts/main_parallel_step4.py" "$path_align_all"
