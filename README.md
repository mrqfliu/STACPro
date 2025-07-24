# STACPro

A high-efficiency tool for protein structure-based clustering and phylogenetic tree construction, leveraging USalign for accurate structural alignment. Designed to streamline clustering analysis of both predicted and experimental protein structures, supporting reliable evolutionary tree inference for protein function and evolution studies.
<img width="1133" height="851" alt="cluster" src="https://github.com/user-attachments/assets/a7fabf0f-7c45-4617-9e68-57ec35c32950" />

## Overview
STACPro automates protein structural clustering through **USalign-based pairwise similarity calculation** and phylogenetic tree construction. It focuses on simplicity and accuracy, using standard structural alignment metrics to generate reliable clustering results, suitable for both small and large-scale protein structure datasets.

### Key Features:
- **Structural Alignment**: Uses USalign for high-precision protein structure comparison (outputs standard TMscore).
- **Clustering Methods**: Supports `nj` (Neighbor-Joining) and `upgma` for evolutionary tree inference.
- **Parallel Processing**: Accelerates large-scale analysis with multi-thread support.
- **Input Flexibility**: Compatible with both predicted and experimental PDB structures.
- **Python Compatibility**: Supports Python 3.7–3.10.


## Installation

### Prerequisites
- Python 3.7–3.10
- USalign (must be installed and accessible via `usalign_path`; see [USalign installation guide](https://github.com/pylelab/USalign)).
- pip (Python package manager)


### Install Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/mrqfliu/stacpro.git
   cd stacpro
   ```

2. Install via `setup.py`:
   ```bash
   python setup.py install
   ```


## Usage

### Core Workflow
STACPro simplifies structural clustering into three key steps:  
1. Calculate pairwise structural similarity using USalign.  
2. Generate evolutionary trees using NJ or UPGMA.  
3. Derive clusters from the tree (upward/downward clustering).  


### Parallel Execution (For Large Datasets)
Run batch processing with parallel threads using the provided script:  
```bash
bash ./run_stacpro_parallel.sh /path/to/pdb_folder 88  # 88 threads
```


## Similarity Calculation Details
STACPro uses **USalign's default structural alignment results** to generate pairwise similarity scores. USalign computes overall structural similarity (e.g., TMscore, RMSD) between full protein structures, focusing on global alignment quality.  

- **Key Metric**: TMscore (0–1, where 1 indicates identical structures), directly derived from USalign output without additional weighting.  
- **No Confidence-Weighted Adjustment**: The similarity matrix reflects raw USalign results, ensuring consistency with standard structural alignment practices.  


## Applications
- **Protein Family Clustering**: Identify structurally related groups from PDB datasets.  
- **Evolutionary Tree Inference**: Explore structural divergence across proteins.  
- **Functional Prediction**: Guide functional annotation via structural similarity.  
- **Large-Scale Screening**: Efficiently process hundreds of PDB structures with parallel support.  
