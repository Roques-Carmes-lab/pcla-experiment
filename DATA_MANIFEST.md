# Data manifest and provenance

All paths in the **Original source** column are relative to the parent working directory, `Figures for Paul's paper/`. SHA-256 hashes allow the selected copies to be compared with their originals.

| Repository file | Original source | SHA-256 | Role |
|---|---|---|---|
| `data/figure1/ADAMopt_data_dict_2025-12-08_11-55-02.npy` | `Figure 1/data/ADAMopt_data_dict_2025-12-08_11-55-02.npy` | `307112e9ee6bdcaa6ffc093fe83870e2aa92ee14901eb4069dcd1bc785dcdf80` | Figure 1 optimizer history and interferograms |
| `data/figure2/tomo_benchmark_2025-12-19_23-23-33.npy` | `Figure 2/data/12192025/tomo_benchmark_2025-12-19_23-23-33.npy` | `80a43f49cd1af0c6e2123c078d9ec392dec8e345fdc95f20ce54b28a5886850c` | Figure 2 tomography, optimization histories, and fringe sweeps |
| `data/figure2/heater_calibration.csv` | Ten exact `(v_bar, v_cross)` pairs extracted from `Figure 2/MZI_calibration_9by9.pkl` | See note below | Minimal voltage-to-phase calibration for Figure 2 fidelity |
| `data/figure3/spatial_sweep_2026-01-15_02-17-24.npy` | `Figure 3/data/01152026/spatial_sweep_2026-01-15_02-17-24.npy` | `a71328d291bd3ce4c3328eb349be7333609712da1c3c84007c74cbd36808332a` | Figure 3 position sweep, grating powers, and optimized eigenvalues |
| `data/figure4/beam_data_dict_2025-12-16_16-32-19.npy` | `Figure 4/data/12162025/beam_data_dict_2025-12-16_16-32-19.npy` | `495ea5dcc2d6a0e3b5b931c4f35456627548d562e5807940106dceab4af14ccb` | Figure 4 input modal weights |
| `data/figure4/Fourierexpt_data_dict_2025-12-16_14-58-22.npy` | `Figure 4/data/12162025/Fourierexpt_data_dict_2025-12-16_14-58-22.npy` | `3885855d53c4c3475d26729be5c8d1ce8cea1d991775d9fd2949e79211f22f54` | Figure 4 optimized output-mode signals |
| `data/figure4/FourierSweep_data_dict_2025-12-17_06-27-35.npy` | `Figure 4/data/12172025_Sweep/FourierSweep_data_dict_2025-12-17_06-27-35.npy` | `471eba2407b79e3432b21d7180cf6071a290fbc73682fb6099744a389c258c4d` | Figure 4 PCLA sweep: eigenvalues, output powers, uncertainties |
| `data/figure4/beam_sweep_lockinA_2025-12-17_07-44-20.npy` | `Figure 4/data/12172025_Sweep/beam_sweep_lockinA_2025-12-17_07-44-20.npy` | `24a9dc454e25217fabf9642c2203150afa0395e81880293086850a42f0f08584` | Figure 4 direct overlap sweep used for the theory fit |
| `figures/reference/Figure1.pdf` | `Figure 1/Figure1_chip_final.pdf` | `aeeef33d6f1d0f20a062a601a21c894424dd00be837bbb196ad81135eaf16eb4` | Final Figure 1 layout reference |
| `figures/reference/Figure2.pdf` | `Figure 2/Figure2.pdf` | `2bca5a9c92c6c0a95b337a64baeeefde87db0f8186c2039b445328c9de500077` | Final Figure 2 layout reference |
| `figures/reference/Figure3.pdf` | `Figure 3/Figure3.pdf` | `4536a033a714878e5e01a717192a2f93e041493b6fb4eb39bcd9654720676db2` | Final Figure 3 layout reference |
| `figures/reference/Figure4.pdf` | `Figure 4/Figure4.pdf` | `e5e5617de7f8725e79682630b7c62fb0b850ff1300613fcce450c2ffce75f768` | Final Figure 4 layout reference |
| `data/si_3pcla/three_pcla_measurements.npz` | Minimal extraction from `SI_Figures/3PCLA/3_laser_contrast_and_convergence.pkl` plus tomography vectors in `3_Laser_Make_Figures.ipynb` | `01d2fd9a519b1b32854f4d44b3780f1fb9efa28a757925d647ba66e556bd59fe` | Raw pairwise interferograms, convergence histories, and plotted three-mode tomography |
| `data/si_3pcla/chip_photo.jpg` | `SI_Figures/3PCLA/IMG_0079.jpg` | `082b0339b9cc2c55cd0878a4502185ad07caf104dcc0a2e11658f6da413fae03` | Photograph used in the 3PCLA figure |
| `data/si_beam_overlap_fourier/camera_averages.npz` | Arithmetic means of all 101 PNG frames at each of six settings in `SI_Figures/Beam_overlap_Fourier/data/12102025/Beam sweep Fourier 2/` | `8c1526ff20c885bb76aef8fd17a728eabe93faec0b35e7f05a18b9439b64a4a9` | Reference beam and five translated-beam camera averages |
| `data/si_beam_overlap_fourier/beam_sweep_lockinA_2025-12-10.npy` | `SI_Figures/Beam_overlap_Fourier/data/12102025/beam_sweep_lockinA (1).npy` | `8d613a2cb44b2c2a7c37ec45604bcf922a2d0d60f2e90b60a160199ae1512caa` | Direct two-beam overlap sweep |
| `data/si_beam_overlap_fourier/coupling_sweep_2025-12-10.npy` | `SI_Figures/Beam_overlap_Fourier/data/12102025/coupling_sweep.npy` | `62416fcaed2b28bf8bd24fa89a79f0ba456acee19f9d6a33db908fb911909e9e` | Total chip-coupling sweep |
| `data/si_pclg/camera_averages.npz` | Exact copies of five `*_avg.npy` arrays in `Figure 2/data/02042026/pclg_02042026/averaged/` | `a8724f43b2e23397c766851104cadb02799036429e1232dc067135497b09b7c8` | Averaged reference and PCLG camera exposures |
| `data/si_pclg/heater_calibration.csv` | 26 exact `(v_bar, v_cross)` pairs extracted from `Figure 2/MZI_calibration_9by9.pkl` | `8a07d8af815d6c44ff6f42ffc3468bbf291ac85f34c8ab110a510c81e0c15607` | Minimal voltage-to-phase calibration for the two PCLG layers |
| `data/si_pclg/pclg_2026-02-04_16-55-08.npy` | `Figure 2/data/02042026/pclg_2026-02-04_16-55-08.npy` | `ba5c9ae332e7f1beab3209806ea2b90ce19b58c05d2dd13820cc2dea59466965` | PCLG optimization histories, powers, and tomography |
| `data/si_pclg/ref_avg_annotated.png` | `Figure 2/data/02042026/pclg_02042026/averaged/ref_avg_annotated.png` | `e4f086c7bccd05778e05b4d62e71a63abbc589e7b8b829182d6e1c3aeaae6e9d` | ROI annotations used to recover the nine camera masks |
| `figures/reference/SI_3PCLA.pdf` | `SI_Figures/3PCLA/pcla_3modes.pdf` | `e1f2a327009f471373a8368a9fb3a163e4c2c607c1d1652acd59a61ba8d1f973` | Final 3PCLA layout reference |
| `figures/reference/SI_Beam_overlap_Fourier.pdf` | `SI_Figures/Beam_overlap_Fourier/beam_overlap_fourier.pdf` | `dff1febf18de44cc86f0ca627f65e596c419a8c3f01c674b1ebc8809c8846d26` | Final beam-overlap layout reference |
| `figures/reference/SI_Figure4_multistart_fits.pdf` | `SI_Figures/Fig4-fits.pdf` | `ae1a0a225fa5977d7ac6cf1d9bd2e1647518a1d1712b09aaf74417e17ad45669` | Final multistart-fit layout reference |
| `figures/reference/SI_PCLG.pdf` | `SI_Figures/PCLG.pdf` | `b0e308e62e01bf6167fb679f1a54375536e97a619f370c58fb46278b7dc07e61` | Final PCLG layout reference |

The parent calibration pickle has SHA-256 `dcf0516412ac19ac2ed6b5d29c39efa59764fad7191b34249fde48228df78745`. The CSV contains its `calibration1535[channel]['v_bar']` and `['v_cross']` values for channels 4, 5, 6, 8, 9, 34, 35, 36, 42, and 43, without numerical rounding.

The 3PCLA parent pickle has SHA-256 `586f3324c263fb9aaa63cd35b14a79458d5ebb36dafca4e0e39a0c39542e3afa`. Its reduced NPZ retains only the initial/final raw voltage and signal vectors for laser pairs 1-2, 1-3, and 2-3, together with the three lock-in convergence histories. The four tomography arrays are transcribed at full displayed precision from the source plotting notebook.

The SI camera NPZ files are deterministic reductions: the Beam-overlap bundle stores arithmetic means of every source frame, while the PCLG bundle packages the five already-averaged source arrays without further numerical processing. The PCLG calibration subset is drawn from the same full-chip calibration pickle identified above and preserves Python floating-point representations without rounding.

## Source notebook mapping

| Clean notebook | Working notebook(s) distilled |
|---|---|
| `01_figure1.ipynb` | `Figure 1/data/Figure1_plots.ipynb` |
| `02_figure2.ipynb` | `Figure 2/12182025_benchmark.ipynb` (despite the filename, it loads the December 19 run) |
| `03_figure3.ipynb` | `Figure 3/20260115_spatial_sweep_analysis.ipynb` |
| `04_figure4.ipynb` | `Figure 4/12162025_Fourier_data_analysis2.ipynb` for panel e and `Figure 4/01132026_theory_Figure4-simplified.ipynb` for the authoritative panels d/f fit |
| `si_01_3pcla.ipynb` | `SI_Figures/3PCLA/3_Laser_Make_Figures.ipynb` and the final assembly logic in `make_compiled_3x2_figure.py` |
| `si_02_beam_overlap_fourier.ipynb` | `SI_Figures/Beam_overlap_Fourier/Fourier_alignment.ipynb` |
| `si_03_figure4_multistart_sensitivity.ipynb` | `Figure 4/01132026_theory_Figure4_multistart_sensitivity.ipynb` and its helper `multistart_fit_analysis.py` |
| `si_04_pclg.ipynb` | `Figure 2/pclg.ipynb` |
