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
|mth5_observations_during_storm2015.ipynb             | Example of getting mth5 data during multiple storms in 2015               |
|mth5_observations_eclipse2017.ipynb                  | Exmaple of mth5 data from ZU stations during solar eclipse in 2017        |
|mth5_observations_May2024_storm.ipynb                | Exmaple of mth5 data during May 10-13 2024 storms                         |


# Installation note
If you would like to execute the examples you need to install `pyspedas` and `mth5` packages. In addition, you need to have `jupyter` packed installed:
```
pip install pyspedas
pip install mth5
pip install jupyter
```


# Installation from git repositories
If you encounter an installation problem, you can try to install packages from git repositories, including `mt_metadata`.   

```
pip install git+https://github.com/spedas/pyspedas.git
pip install git+https://github.com/kujaku11/mt_metadata.git
pip install git+https://github.com/kujaku11/mth5.git
```

