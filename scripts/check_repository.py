#!/usr/bin/env python3
"""Verify that the experimental data files are unchanged."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EXPECTED = {
    "data/figure1/ADAMopt_data_dict_2025-12-08_11-55-02.npy": "307112e9ee6bdcaa6ffc093fe83870e2aa92ee14901eb4069dcd1bc785dcdf80",
    "data/figure2/tomo_benchmark_2025-12-19_23-23-33.npy": "80a43f49cd1af0c6e2123c078d9ec392dec8e345fdc95f20ce54b28a5886850c",
    "data/figure2/heater_calibration.csv": "4e36407fbdac4247d8867bd3d977a45453a899a788ef439c9eee0087cb90b9ac",
    "data/figure3/spatial_sweep_2026-01-15_02-17-24.npy": "a71328d291bd3ce4c3328eb349be7333609712da1c3c84007c74cbd36808332a",
    "data/figure4/beam_data_dict_2025-12-16_16-32-19.npy": "495ea5dcc2d6a0e3b5b931c4f35456627548d562e5807940106dceab4af14ccb",
    "data/figure4/Fourierexpt_data_dict_2025-12-16_14-58-22.npy": "3885855d53c4c3475d26729be5c8d1ce8cea1d991775d9fd2949e79211f22f54",
    "data/figure4/FourierSweep_data_dict_2025-12-17_06-27-35.npy": "471eba2407b79e3432b21d7180cf6071a290fbc73682fb6099744a389c258c4d",
    "data/figure4/beam_sweep_lockinA_2025-12-17_07-44-20.npy": "24a9dc454e25217fabf9642c2203150afa0395e81880293086850a42f0f08584",
    "data/si_3pcla/chip_photo.jpg": "082b0339b9cc2c55cd0878a4502185ad07caf104dcc0a2e11658f6da413fae03",
    "data/si_3pcla/three_pcla_measurements.npz": "01d2fd9a519b1b32854f4d44b3780f1fb9efa28a757925d647ba66e556bd59fe",
    "data/si_beam_overlap_fourier/beam_sweep_lockinA_2025-12-10.npy": "8d613a2cb44b2c2a7c37ec45604bcf922a2d0d60f2e90b60a160199ae1512caa",
    "data/si_beam_overlap_fourier/camera_averages.npz": "8c1526ff20c885bb76aef8fd17a728eabe93faec0b35e7f05a18b9439b64a4a9",
    "data/si_beam_overlap_fourier/coupling_sweep_2025-12-10.npy": "62416fcaed2b28bf8bd24fa89a79f0ba456acee19f9d6a33db908fb911909e9e",
    "data/si_pclg/camera_averages.npz": "a8724f43b2e23397c766851104cadb02799036429e1232dc067135497b09b7c8",
    "data/si_pclg/heater_calibration.csv": "8a07d8af815d6c44ff6f42ffc3468bbf291ac85f34c8ab110a510c81e0c15607",
    "data/si_pclg/pclg_2026-02-04_16-55-08.npy": "ba5c9ae332e7f1beab3209806ea2b90ce19b58c05d2dd13820cc2dea59466965",
    "data/si_pclg/ref_avg_annotated.png": "e4f086c7bccd05778e05b4d62e71a63abbc589e7b8b829182d6e1c3aeaae6e9d",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    failures = []
    for relative, expected in EXPECTED.items():
        path = ROOT / relative
        if not path.is_file():
            failures.append(f"MISSING  {relative}")
            continue
        actual = sha256(path)
        if actual != expected:
            failures.append(f"CHANGED  {relative}\n  expected {expected}\n  actual   {actual}")
        else:
            print(f"OK       {relative}")

    if failures:
        print("\n".join(failures))
        return 1
    print(f"\nVerified {len(EXPECTED)} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
