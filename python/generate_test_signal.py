
from pathlib import Path

import numpy as np

FS = 100_000
DURATION = 0.020
Q15_MAX = 32767

NUM_SAMPLES = int(FS * DURATION)
n = np.arange(NUM_SAMPLES)

# Equal-amplitude 1 kHz and 10 kHz sine waves.
signal = 0.5 * np.sin(2 * np.pi * 1_000 * n / FS)
signal += 0.5 * np.sin(2 * np.pi * 10_000 * n / FS)

# Convert to signed Q15 integer samples.
samples_q15 = np.round(signal * Q15_MAX).astype(np.int32)

# Check the signed 16-bit range.
assert np.all(samples_q15 >= -32768)
assert np.all(samples_q15 <= 32767)

project_dir = Path(__file__).resolve().parent.parent
results_dir = project_dir / "results"
results_dir.mkdir(parents=True, exist_ok=True)

# Save one decimal integer per line for Verilog $readmemh is
# not appropriate for signed decimal samples, so use decimal text.
input_path = results_dir / "mixed_signal_q15.txt"
np.savetxt(input_path, samples_q15, fmt="%d")

# Save sample index, input integer, and normalized input value.
csv_path = results_dir / "mixed_signal_q15.csv"
np.savetxt(
    csv_path,
    np.column_stack((n, samples_q15, samples_q15 / Q15_MAX)),
    delimiter=",",
    header="sample_index,input_q15,input_normalized",
    comments="",
    fmt=["%d", "%d", "%.8f"],
)

print("Mixed-frequency test signal generated.")
print(f"Sampling frequency: {FS} Hz")
print("Tone frequencies: 1000 Hz and 10000 Hz")
print(f"Number of samples: {NUM_SAMPLES}")
print(f"Input range: {samples_q15.min()} to {samples_q15.max()}")
print(f"Integer samples: {input_path}")
print(f"CSV reference: {csv_path}")
