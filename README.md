# PCLA experiment data and figure reproduction

This repository contains the experimental data and Jupyter notebooks used to reproduce the data-driven panels in main-text Figures 1-4 and selected supplementary figures of the PCLA paper.

Paper: [arXiv:2603.15517](https://arxiv.org/abs/2603.15517)

## Repository layout

```text
data/               Experimental data, grouped by figure
notebooks/          Reproducible plotting notebooks
figures/generated/  PNG outputs produced by the notebooks
scripts/            Repository validation utilities
```

## Reproduce the figures

Create the environment with Conda:

```bash
conda env create -f environment.yml
conda activate pcla-experiment
jupyter lab
```

Alternatively, use `pip`:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab
```

Start Jupyter from anywhere inside the repository and run the notebooks in numerical order. Each notebook automatically locates the repository root and writes its PNG output to `figures/generated/`.

The `.npy` files contain pickled Python dictionaries and are loaded with `allow_pickle=True`. Only load data obtained from a trusted copy of this repository.

## Figure map

### Main text

| Figure | Notebook | Generated output | Content reproduced |
|---|---|---|---|
| 1 | `01_figure1.ipynb` | `figure1_optimization_panels.png` | Parallel gradients, phase-shifter trajectories, and interferograms during self-configuration |
| 2 | `02_figure2.ipynb` | `figure2_benchmark_panels.png` | Modal fidelity, recovered eigenvalues, and residual output-interferogram visibility |
| 3 | `03_figure3.ipynb` | `figure3_intensity_maps.png`, `figure3_sweep_panels.png` | Four-port intensity maps, PCLA eigenvalues, and entropy versus beam position |
| 4 | `04_figure4.ipynb` | `figure4_mode_separation.png`, `figure4_dot_product_fit.png`, `figure4_fourier_operation.png` | Input/output modal weights, overlap fit, Fourier-domain entropy, and cross-talk |

### Supplementary information

| Figure | Notebook | Generated output | Content reproduced |
|---|---|---|---|
| 3PCLA | `si_01_3pcla.ipynb` | `si_3pcla.png` | Three-mode tomography, convergence, pairwise interferograms, and chip photograph |
| Beam overlap Fourier | `si_02_beam_overlap_fourier.ipynb` | `si_beam_overlap_fourier.png` | Five camera overlays and the coupling/overlap position sweep |
| Figure 4 fit sensitivity | `si_03_figure4_multistart_sensitivity.ipynb` | `si_figure4_multistart_sensitivity.png` | Multistart fits and phase-equivalent cross-talk branches |
| PCLG | `si_04_pclg.ipynb` | `si_pclg_quantitative_panels.png` | Camera intensity map and measured/model modal weights |

Run `python scripts/check_repository.py` to verify the included experimental data before plotting.

## Contact

Charles Roques-Carmes, Institute of Science and Technology Austria, [crc@ista.ac.at](mailto:crc@ista.ac.at)
