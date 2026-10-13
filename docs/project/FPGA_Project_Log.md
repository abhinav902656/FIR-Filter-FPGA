# FPGA Project Log

## Project Information

- **College project title:** FPGA Implementation of Optimized FIR Filter for Signal Processing
- **Paper title:** Design and FPGA Implementation of Area-Speed Optimized Pipelined FIR Filter Architectures for Real-Time Signal Processing
- **College:** Galgotias College of Engineering and Technology
- **Current architecture:** Direct Form FIR
- **Status:** Linux simulation and reference comparison completed

## 1. Fixed Filter Specifications

- Filter type: 8-tap Hamming low-pass FIR
- Sampling frequency: 100 kHz
- Cutoff frequency: 5 kHz
- Input format: Signed 16-bit Q15
- Output format: Signed 32-bit
- Test signal: Sum of 1 kHz and 10 kHz sine waves
- HDL: Verilog

## 2. Coefficient Generation

The FIR coefficients were generated using Python and SciPy.

Q15 integer coefficients:

`570, 2006, 5445, 8363, 8363, 5445, 2006, 570`

Checks completed:

- Coefficient symmetry: True
- Sum of Q15 integer coefficients: 32768
- CSV coefficient file generated
- Frequency-response plot generated

## 3. Direct Form Implementation

Source file: `src/fir_direct.v`

The design uses seven delay registers, eight coefficient multiplications, an accumulator, and a registered output.

The design uses synchronous reset. Sequential assignments use non-blocking assignments, and combinational calculations use blocking assignments.

## 4. Output-Scaling Decision

The current design retains the raw integer coefficient-product sum.

The products of signed Q15 input integers and Q15 coefficient integers have Q30 fractional scale. The output is not shifted back to Q15.

All four architectures must use the same output-scaling convention for a fair comparison. See `Output_Scaling_Decision.md` for the detailed reasoning and numeric-range calculation.

## 5. Verification Results

### Impulse and Reset Test

Testbench: `testbench/tb_fir_direct.v`

Results:

- All eight impulse-response tap values matched the expected values.
- Synchronous reset cleared the output.
- Synchronous reset cleared the delay line.
- Final result: PASS.

### Full-Range Input Test

Testbench: `testbench/tb_fir_direct_range.v`

Inputs checked: 32767, -32768, 0, and 1.

All four outputs matched their expected values.

Final result: PASS.

### Mixed-Frequency Test

Testbench: `testbench/tb_fir_direct_mixed.v`

- Input signal: 1 kHz plus 10 kHz sine waves
- Number of input samples: 2000
- Number of output samples: 2000
- Simulation completed successfully

### Python Reference Comparison

The Verilog outputs were compared with an integer convolution reference using the same Q15 integer coefficients and raw product-sum convention.

- Maximum absolute error: 0
- Mismatched samples: 0
- Final result: PASS.

## 6. Frequency Response

Measured response using the quantized coefficients:

| Frequency | Gain | Response |
|---|---:|---:|
| 1 kHz | 0.995928 | -0.04 dB |
| 5 kHz | 0.902637 | -0.89 dB |
| 10 kHz | 0.660348 | -3.60 dB |

The 1 kHz tone passes with little attenuation. The 10 kHz tone is attenuated, but not removed completely. The filter's limited stopband attenuation must be considered when discussing performance.

## 7. Generated Files

- `python/fir_coefficients.py`
- `python/generate_test_signal.py`
- `results/fir_coefficients_q15.csv`
- `results/mixed_signal_q15.txt`
- `results/mixed_signal_q15.csv`
- `results/plots/fir_direct_frequency_response.png`
- `results/simulation/fir_direct.vcd`
- `results/simulation/fir_direct_mixed.vcd`
- `results/simulation/fir_direct_mixed_output.txt`

## 8. Current Status and Next Steps

Completed:

- Direct Form RTL implementation
- Coefficient generation
- Impulse and reset simulation
- Full-range input test
- Mixed-frequency simulation
- Python reference comparison
- GTKWave waveform inspection
- Output-scaling decision documentation

Not yet completed:

- Final Git review and commit
- FPGA synthesis and implementation
- Area and timing measurement
- Comparison against the other three architectures

The Direct Form architecture has passed the current Linux simulation tests. FPGA synthesis and hardware implementation remain separate verification steps.
