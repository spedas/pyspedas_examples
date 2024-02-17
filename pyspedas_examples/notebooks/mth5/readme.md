# PySPEDAS MTH5 examples

This folder contains Jupyter notebooks illustrating how to work with PySPEDAS mth5 tool.
mth5 tools allow user to load ground-based magnetic field measurements from International Federation of Digital Seismographic Networks.

| Notebook                                            | Description                                                               |
|-----------------------------------------------------|---------------------------------------------------------------------------|
| load_fdsn_example.ipynb                             | Basic example of loading and plotting data from FDSN network              |
| explore_station_availability.ipynb                  | Instruction of how to explore availability of the stations                |
| comparison_with_published_results.ipynb             | Step-by-step guide of mth5 tool use and comparison with published results |
| miniGEM2023_load_fdsn_example.ipynb                 | Notebook presented at min-GEM 2023                                        |
| THEMIS-ARTEMIS-Post-AGU2023_load_fdsn_example.ipynb | Notebook presented at THEMIS/ARTEMIS Post AGU 2023                        |

# Installation note

PySPEDAS mth5 tool is under active development. If you would like to execute the examples you need to install appropriate `pyspedas` (mth5 branch), `mt_metadata` (main branch), and `mth5` (master branch) packages.
```
pip install git+https://github.com/spedas/pyspedas.git@mth5
pip install git+https://github.com/kujaku11/mt_metadata.git
pip install git+https://github.com/kujaku11/mth5.git
```

In addition, you need to have `jupyter` packed installed:
```
pip install jupyter
```
