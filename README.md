# PCLA figure reproduction

This repository contains the minimal experimental data and plotting notebooks needed to regenerate the data-driven panels in main-text Figures 1-4 and four selected supplementary figures of the PCLA paper.

The original working folders contain acquisition notebooks, intermediate runs, camera-frame stacks, duplicated analyses, presentation variants, and draft figures. Those files are intentionally excluded here. The publication PDFs are retained under `figures/reference/` so that regenerated panels can be checked against the final layout.

## Repository layout

```text
data/                 Selected raw or losslessly reduced experimental data
notebooks/            Focused, portable plotting notebooks
figures/reference/    Final main-text and selected SI PDFs
figures/generated/    Notebook outputs (ignored by Git except for .gitkeep)
scripts/              Lightweight repository validation
DATA_MANIFEST.md      Source mapping, checksums, and selection rationale
```

## Reproduce the plots

Create the environment with either Conda or `pip`:

```bash
conda env create -f environment.yml
conda activate pcla-main-text-figures
jupyter lab
```

or:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab
```

Open Jupyter from the repository root and run the notebooks in numerical order. Each notebook locates the repository root automatically and writes SVG and PNG outputs to `figures/generated/`.

The `.npy` files contain pickled Python dictionaries and are therefore loaded with `allow_pickle=True`. Only load copies obtained from a trusted source.

## Figure map

### Main text

| Figure | Notebook output | Experimental content regenerated |
|---|---|---|
| 1 | `figure1_optimization_panels.*` | Parallel gradients, phase-shifter trajectories, and interferograms during self-configuration (panels g-i) |
| 2 | `figure2_benchmark_panels.*` | Modal fidelity, recovered eigenvalues, and residual output-interferogram visibility (panels c-e) |
| 3 | `figure3_intensity_maps.*`, `figure3_sweep_panels.*` | Four-port intensity maps, PCLA eigenvalues, and entropy versus beam position (panels b-d) |
| 4 | `figure4_mode_separation.*`, `figure4_dot_product_fit.*`, `figure4_fourier_operation.*` | Input/output modal weights, overlap fit, Fourier-domain entropy, and cross-talk (panels d-f) |

### Supplementary information

| Figure | Notebook | Notebook output | Content regenerated |
|---|---|---|---|
| 3PCLA | `si_01_3pcla.ipynb` | `si_3pcla.*` | Three-mode tomography, convergence, pairwise interferograms, and chip photograph |
| Beam overlap Fourier | `si_02_beam_overlap_fourier.ipynb` | `si_beam_overlap_fourier.*` | Five camera overlays and the coupling/overlap position sweep |
| Figure 4 fit sensitivity | `si_03_figure4_multistart_sensitivity.ipynb` | `si_figure4_multistart_sensitivity.*` | Twenty multistart fits, grouped into five phase-equivalent cross-talk branches |
| PCLG | `si_04_pclg.ipynb` | `si_pclg_quantitative_panels.*` | Camera intensity map and measured/model modal weights (published panels c-f) |

The illustrative, photographic, and device-layout panels were assembled outside the plotting notebooks. Their editable composition files are not present in the original Figure 1-4 folders; the final PDFs in `figures/reference/` preserve those panels and their layout. The notebooks reproduce every quantitative plot used in those PDFs without depending on the original absolute paths or the laboratory-control stack.

## Notes on the minimal selection

- Figure 1 uses the final December 8 optimization run. The separate beam-balance file and two earlier optimization runs are diagnostics and do not feed the published panels.
- Figure 2 uses the December 19 benchmark run. The large February camera-acquisition directory belongs to a later PCL-generation analysis and is not used by the published Figure 2 PDF.
- Figure 2 originally read a 19 MB full-chip calibration pickle. Only `v_bar` and `v_cross` for the ten phase shifters used by the two plotted layers are required, so those values are preserved losslessly in `heater_calibration.csv`.
- Figure 3 uses the January 15 sweep dictionary. The 400+ camera frames in the working folder were used for a separate overlay diagnostic; the published intensity maps are rendered directly from the four measured grating-coupler powers stored in the sweep dictionary.
- Figure 4 needs two small December 16 files for the input/output bars and two December 17 sweep files for the overlap fit, entropy, and cross-talk. Its optical fit follows `01132026_theory_Figure4-simplified.ipynb`: a 120 µm input-beam radius and one omitted grating-coupler port are fixed, five optical parameters are fitted to the overlap sweep, and one incoherent-background parameter is fitted to the entropy data. The intensity-sweep file is only a beam-diameter sanity check and is excluded.
- The 3PCLA notebook replaces a 701 MB analysis pickle with a 5.2 MB bundle containing only the raw interferogram traces, convergence histories, and the four plotted tomography vectors. Smoothed traces and acquisition state are excluded.
- Beam-overlap camera data are exact arithmetic averages of the 101 frames at each of the six plotted settings, reducing 606 PNGs to one compact array bundle. The published plot uses the December 10 overlap sweep (`beam_sweep_lockinA (1).npy`), not the later December 15 diagnostic loaded in one active working-notebook cell.
- The Figure 4 multistart notebook reuses the two Figure 4 sweep files already included for the main text; no duplicate data are stored.
- PCLG camera data are the five exact averaged arrays used by the source notebook, replacing 505 individual frames. The calibration CSV contains only the 26 heater entries required by the two plotted layers. Conceptual panels (a-b) were assembled outside the analysis notebook and remain available in the reference PDF.

Run `python scripts/check_repository.py` to verify the data and reference-PDF checksums before plotting.

## License and citation

No publication license or final paper citation was present in the working folders. Add the authors' chosen license and citation metadata before making the repository public.
