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
PLOT_DIR = ROOT / "results/plots"

FS = 100_000
EXPECTED_SAMPLES = 2000
Q15_SCALE = 32768
Q30_SCALE = 2**30


def main():
    # Check required files before loading data.
    required = (COEFF_FILE, INPUT_FILE, OUTPUT_FILE)
    for path in required:
        if not path.is_file():
            print(f"ERROR: Required file not found: {path.relative_to(ROOT)}")
            return 1

    # Read coefficients from the Q15 integer column of the CSV.
    coefficients = np.loadtxt(
        COEFF_FILE, delimiter=",", skiprows=1, usecols=1, dtype=np.int64
    )
    inputs = np.loadtxt(INPUT_FILE, dtype=np.int64, ndmin=1)
    outputs = np.loadtxt(OUTPUT_FILE, dtype=np.int64, ndmin=1)

    if len(coefficients) != 8:
        print(f"ERROR: Expected 8 coefficients, found {len(coefficients)}.")
        return 1

    if len(inputs) != EXPECTED_SAMPLES or len(outputs) != EXPECTED_SAMPLES:
        print(
            f"ERROR: Expected {EXPECTED_SAMPLES} input and output samples; "
            f"found {len(inputs)} inputs and {len(outputs)} outputs."
        )
        return 1

    PLOT_DIR.mkdir(parents=True, exist_ok=True)

    # Convert the input and raw Q30-scaled output to comparable amplitudes.
    input_normalized = inputs.astype(np.float64) / Q15_SCALE
    output_normalized = outputs.astype(np.float64) / Q30_SCALE
    time_ms = np.arange(len(inputs)) / FS * 1000.0

    # A3: Input and filtered output on the same time axis.
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(time_ms, input_normalized, label="Input (Q15 / 32768)",
            linewidth=1.0)
    ax.plot(time_ms, output_normalized, label="Filtered output (raw / 2^30)",
            linewidth=1.0)
    ax.set_title("Direct Form FIR: Input vs Filtered Output")
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Normalized amplitude")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(PLOT_DIR / "fir_direct_input_vs_output_time.png",
                dpi=200, bbox_inches="tight")
    plt.close(fig)

    # A4: FFT magnitude comparison after skipping the first 8 samples.
    skip = 8
    spectrum_input = input_normalized[skip:]
    spectrum_output = output_normalized[skip:]
    window = np.hanning(len(spectrum_input))

    fft_input = np.fft.rfft(spectrum_input * window)
    fft_output = np.fft.rfft(spectrum_output * window)
    frequencies = np.fft.rfftfreq(len(spectrum_input), d=1.0 / FS)

    # Normalize by the window sum to make the amplitude scale meaningful.
    input_mag = 2.0 * np.abs(fft_input) / np.sum(window)
    output_mag = 2.0 * np.abs(fft_output) / np.sum(window)

    eps = np.finfo(np.float64).tiny
    input_db = 20.0 * np.log10(np.maximum(input_mag, eps))
    output_db = 20.0 * np.log10(np.maximum(output_mag, eps))

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(frequencies / 1000.0, input_db, label="Input spectrum",
            linewidth=1.0)
    ax.plot(frequencies / 1000.0, output_db, label="Output spectrum",
            linewidth=1.0)
    ax.axvline(1.0, linestyle="--", linewidth=1.0, label="1 kHz")
    ax.axvline(10.0, linestyle=":", linewidth=1.2, label="10 kHz")
    ax.set_title("Direct Form FIR: Input vs Output Spectrum")
    ax.set_xlabel("Frequency (kHz)")
    ax.set_ylabel("Magnitude (dB relative to normalized amplitude 1)")
    ax.set_xlim(0, FS / 2 / 1000.0)
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(PLOT_DIR / "fir_direct_spectrum_input_vs_output.png",
                dpi=200, bbox_inches="tight")
    plt.close(fig)

    # Measure gain near each test tone using the same window for both signals.
    print("Measured spectrum gain after skipping the first 8 samples:")
    measured_gains = {}
    for tone_hz, expected_gain in ((1000.0, 0.9959), (10000.0, 0.6603)):
        tone_bin = int(np.argmin(np.abs(frequencies - tone_hz)))
        input_amplitude = input_mag[tone_bin]
        output_amplitude = output_mag[tone_bin]
        gain = (
            output_amplitude / input_amplitude
            if input_amplitude > 0 else float("nan")
        )
        measured_gains[int(tone_hz)] = gain
        print(
            f"{tone_hz / 1000:.0f} kHz: {gain:.4f} "
            f"(reference about {expected_gain:.4f}; "
            f"FFT bin {frequencies[tone_bin]:.2f} Hz)"
        )

    # A5: Theoretical 8-tap impulse response derived from the Q15 coefficients.
    # This is the coefficient-defined response, not a newly measured simulation.
    tap_indices = np.arange(len(coefficients))
    impulse_response = coefficients.astype(np.float64) / Q15_SCALE

    fig, axes = plt.subplots(2, 1, figsize=(12, 8), constrained_layout=True)

    axes[0].stem(tap_indices, impulse_response)
    axes[0].set_title("8-Tap FIR Impulse Response (Q15 Coefficients)")
    axes[0].set_xlabel("Tap index")
    axes[0].set_ylabel("Normalized coefficient")
    axes[0].grid(True, alpha=0.3)

    axes[1].stem(tap_indices, coefficients)
    axes[1].set_title("Impulse Response Coefficients as Q15 Integers")
    axes[1].set_xlabel("Tap index")
    axes[1].set_ylabel("Coefficient (Q15 integer)")
    axes[1].grid(True, alpha=0.3)

    fig.savefig(PLOT_DIR / "fir_direct_impulse_response.png",
                dpi=200, bbox_inches="tight")
    plt.close(fig)

    # A6: Q15 coefficients with tap labels.
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(tap_indices, coefficients, width=0.7, label="Q15 coefficient")
    ax.set_title("Direct Form FIR: Q15 Coefficients")
    ax.set_xlabel("Tap index")
    ax.set_ylabel("Coefficient (Q15 integer)")
    ax.set_xticks(tap_indices)
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(PLOT_DIR / "fir_direct_coefficients_q15.png",
                dpi=200, bbox_inches="tight")
    plt.close(fig)

    print("Generated plots:")
    print(" - results/plots/fir_direct_input_vs_output_time.png")
    print(" - results/plots/fir_direct_spectrum_input_vs_output.png")
    print(" - results/plots/fir_direct_impulse_response.png")
    print(" - results/plots/fir_direct_coefficients_q15.png")

    # Flag a significant disagreement with the expected gains.
    # The tolerance allows for finite-record FFT-bin and window effects.
    tolerance = 0.03
    disagreement = False
    for tone_hz, expected_gain in ((1000, 0.9959), (10000, 0.6603)):
        gain = measured_gains[tone_hz]
        if not np.isfinite(gain) or abs(gain - expected_gain) > tolerance:
            print(
                f"WARNING: Measured gain at {tone_hz / 1000} kHz "
                f"differs from the reference by more than {tolerance:.2f}."
            )
            disagreement = True

    if disagreement:
        print("Review the measured spectrum before accepting the plots.")
        return 1

    print("PASS: Measured gains agree with the expected values within tolerance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
