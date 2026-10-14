#!/usr/bin/env python3

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parent.parent
COEFF_FILE = ROOT / "results/fir_coefficients_q15.csv"
INPUT_FILE = ROOT / "results/mixed_signal_q15.txt"
OUTPUT_FILE = ROOT / "results/simulation/fir_direct_mixed_output.txt"
PLOT_FILE = ROOT / "results/plots/fir_direct_python_vs_verilog.png"


def main():
    for path in (COEFF_FILE, INPUT_FILE, OUTPUT_FILE):
        if not path.is_file():
            print(f"ERROR: Required file not found: {path.relative_to(ROOT)}")
            return 1

    # Read the Q15 integer coefficients from the second CSV column.
    coefficients = np.loadtxt(
        COEFF_FILE, delimiter=",", skiprows=1, usecols=1, dtype=np.int64
    )

    # Read input samples and actual Verilog output as integers.
    inputs = np.loadtxt(INPUT_FILE, dtype=np.int64, ndmin=1)
    verilog_output = np.loadtxt(OUTPUT_FILE, dtype=np.int64, ndmin=1)

    if len(inputs) != len(verilog_output):
        print(
            "ERROR: Input/output length mismatch: "
            f"{len(inputs)} inputs, {len(verilog_output)} outputs."
        )
        return 1

    if len(inputs) != 2000:
        print(f"ERROR: Expected 2000 input samples, found {len(inputs)}.")
        return 1

    # Integer reference. The RTL uses the raw Q30-scaled product sum.
    reference = np.convolve(
        inputs.astype(np.int64),
        coefficients.astype(np.int64),
        mode="full",
    )[:len(inputs)].astype(np.int64)

    error = verilog_output - reference
    max_error = int(np.max(np.abs(error))) if len(error) else 0
    mismatches = int(np.count_nonzero(error))

    print(f"Input samples: {len(inputs)}")
    print(f"Verilog output samples: {len(verilog_output)}")
    print(f"Q15 coefficients: {len(coefficients)}")
    print(f"Input range: {int(inputs.min())} to {int(inputs.max())}")
    print(f"Max absolute error: {max_error}")
    print(f"Mismatches: {mismatches}")

    # Create the three-panel comparison plot.
    PLOT_FILE.parent.mkdir(parents=True, exist_ok=True)
    sample_count = min(200, len(inputs))
    sample_index = np.arange(sample_count)

    fig, axes = plt.subplots(3, 1, figsize=(12, 9), constrained_layout=True)

    axes[0].plot(np.arange(len(inputs)), inputs, linewidth=0.8)
    axes[0].set_title("Direct Form FIR: Input Samples")
    axes[0].set_xlabel("Sample index (samples)")
    axes[0].set_ylabel("Input (Q15 integer)")
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(
        sample_index, reference[:sample_count],
        label="Python reference", linewidth=1.2
    )
    axes[1].plot(
        sample_index, verilog_output[:sample_count],
        label="Verilog output", linestyle="--", linewidth=1.0
    )
    axes[1].set_title("Python Reference vs Verilog Output (First 200 Samples)")
    axes[1].set_xlabel("Sample index (samples)")
    axes[1].set_ylabel("Raw output (Q30-scaled integer)")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    axes[2].plot(np.arange(len(error)), error, linewidth=0.8)
    axes[2].set_title("Verilog Output Error")
    axes[2].set_xlabel("Sample index (samples)")
    axes[2].set_ylabel("Verilog - Python (integer)")
    axes[2].grid(True, alpha=0.3)

    fig.savefig(PLOT_FILE, dpi=200, bbox_inches="tight")
    plt.close(fig)

    print(f"Comparison plot saved: {PLOT_FILE.relative_to(ROOT)}")

    if mismatches:
        print("FAIL: Verilog output differs from the Python reference.")
        return 1

    print("PASS: All Verilog outputs match the Python reference.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
