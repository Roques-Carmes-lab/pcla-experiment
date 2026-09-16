# PCLA experiment data and figure reproduction

This repository contains the experimental data and Jupyter notebooks used to reproduce the data-driven panels in main-text Figures 1-4 and selected supplementary figures of the PCLA paper.

Paper: Mor et al., Separating partially coherent light, [arXiv:2603.15517](https://arxiv.org/abs/2603.15517) (2026)

## Repository layout

```text
data/               Experimental data, grouped by figure
notebooks/          Reproducible plotting notebooks
figures/png/        PNG outputs produced by the notebooks
figures/svg/        Matching SVG outputs produced by the notebooks
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

Start Jupyter from anywhere inside the repository to run the notebooks. Each notebook automatically locates the repository root and writes matching PNG and SVG outputs to `figures/png/` and `figures/svg/`, respectively.

The `.npy` files contain pickled Python dictionaries and are loaded with `allow_pickle=True`.

For Figures 3 and 4, `FINAL_FRACTION` defines the converged portion of each optimization and can be adjusted in the corresponding notebook. Error bars denote one standard deviation. Figure 4 uses this window for the output-mode bars and entropy statistics; its cross-talk uncertainties are propagated from the saved beam-resolved output-channel standard deviations. Figure 2 visibility uncertainties are propagated from the sinusoidal-fit covariance.

## Figure map

### Main text

| Figure | Notebook | Output basename (PNG and SVG) | Content reproduced |
|---|---|---|---|
| 1 | `01_figure1.ipynb` | `figure1_optimization_panels` | Parallel gradients, phase-shifter trajectories, and interferograms during self-configuration |
| 2 | `02_figure2.ipynb` | `figure2_benchmark_panels` | Modal fidelity, recovered eigenvalues, and residual output-interferogram visibility |
| 3 | `03_figure3.ipynb` | `figure3_intensity_maps`, `figure3_sweep_panels` | Four-port intensity maps, PCLA eigenvalues, and entropy versus beam position |
| 4 | `04_figure4.ipynb` | `figure4_mode_separation`, `figure4_dot_product_fit`, `figure4_fourier_operation` | Input/output modal weights, overlap fit, Fourier-domain entropy, and cross-talk |

### Supplementary information

| Figure | Notebook | Output basename (PNG and SVG) | Content reproduced |
|---|---|---|---|
| 3PCLA | `si_01_3pcla.ipynb` | `si_3pcla` | Three-mode tomography, convergence, pairwise interferograms, and chip photograph |
| Beam overlap Fourier | `si_02_beam_overlap_fourier.ipynb` | `si_beam_overlap_fourier` | Five camera overlays and the coupling/overlap position sweep |
| Figure 4 fit sensitivity | `si_03_figure4_multistart_sensitivity.ipynb` | `si_figure4_multistart_sensitivity` | Multistart fits and phase-equivalent cross-talk branches |
| PCLG | `si_04_pclg.ipynb` | `si_pclg_quantitative_panels` | Camera intensity map and measured/model modal weights |

Run `python scripts/check_repository.py` to verify the included experimental data before plotting.

## Contact

Charles Roques-Carmes, Institute of Science and Technology Austria, [crc@ista.ac.at](mailto:crc@ista.ac.at)
