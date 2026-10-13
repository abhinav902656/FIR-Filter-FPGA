
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Fixed project specifications
FS = 100_000
FC = 5_000
NUM_TAPS = 8
Q15_SCALE = 32768

# Design the Hamming-window low-pass FIR filter
coeff_float = firwin(
    numtaps=NUM_TAPS,
    cutoff=FC,
    window="hamming",
    pass_zero="lowpass",
    fs=FS
)

# Convert floating-point coefficients to Q15 integers
coeff_q15 = np.round(coeff_float * Q15_SCALE).astype(np.int32)

# Print the coefficients
print("8-tap Hamming Low-pass FIR")
print(f"Sampling frequency: {FS} Hz")
print(f"Cutoff frequency: {FC} Hz")
print()
print("Tap   Float coefficient   Q15 integer")

for i, (c_float, c_q15) in enumerate(zip(coeff_float, coeff_q15)):
    print(f"{i:2d}    {c_float: .8f}       {c_q15:5d}")

print()
print("Sum of Q15 coefficients:", int(np.sum(coeff_q15)))
print("Coefficient symmetry:", np.array_equal(coeff_q15, coeff_q15[::-1]))

# Locate the project folders
project_dir = Path(__file__).resolve().parent.parent
results_dir = project_dir / "results"
plots_dir = results_dir / "plots"

results_dir.mkdir(parents=True, exist_ok=True)
plots_dir.mkdir(parents=True, exist_ok=True)

# Save the coefficients
csv_path = results_dir / "fir_coefficients_q15.csv"

np.savetxt(
    csv_path,
    np.column_stack((coeff_float, coeff_q15)),
    delimiter=",",
    header="coefficient_float,coefficient_q15",
    comments="",
    fmt=["%.10f", "%d"]
)

print("CSV saved to:", csv_path)

# Calculate the frequency response of the quantized filter
coeff_quantized = coeff_q15.astype(np.float64) / Q15_SCALE

freq, response = freqz(
    coeff_quantized,
    worN=4096,
    fs=FS
)

magnitude_db = 20 * np.log10(np.maximum(np.abs(response), 1e-12))

# Save the frequency response plot
plt.figure(figsize=(9, 5))
plt.plot(freq, magnitude_db)
plt.axvline(FC, linestyle="--", label="5 kHz cutoff")
plt.axvline(10_000, linestyle=":", label="10 kHz test tone")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.title("8-Tap Hamming Low-pass FIR Frequency Response")
plt.grid(True)
plt.legend()
plt.tight_layout()

plot_path = plots_dir / "fir_direct_frequency_response.png"
plt.savefig(plot_path, dpi=300)
plt.close()

print("Frequency response saved to:", plot_path)
print("Coefficient generation completed.")
