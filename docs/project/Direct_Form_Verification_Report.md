# Direct Form FIR Verification Report

## 1. Overview

This report records the functional verification of the Direct Form FIR filter.

The filter uses 8 taps, signed 16-bit Q15 input samples, and signed 32-bit output samples. The testbench checks the impulse response, synchronous reset, and delay-line clearing.

## 2. Impulse Response Verification

The testbench applied an impulse input and checked the eight output tap values.

| Tap | Expected output |
|---:|---:|
| 0 | 18677190 |
| 1 | 65730602 |
| 2 | 178416315 |
| 3 | 274030421 |
| 4 | 274030421 |
| 5 | 178416315 |
| 6 | 65730602 |
| 7 | 18677190 |

All eight tap checks passed.

## 3. Reset Verification

The testbench verified the following conditions:

- Reset cleared the output.
- Reset cleared the delay line.

Both checks passed.

## 4. Python Reference Comparison

The Python integer reference was compared against the Verilog output for 2,000 input samples.

| Measurement | Result |
|---|---:|
| Input samples | 2,000 |
| Verilog output samples | 2,000 |
| Q15 coefficients | 8 |
| Input range | −31,836 to 31,836 |
| Maximum absolute error | 0 |
| Mismatches | 0 |

All compared Verilog outputs matched the Python reference.

## 5. Mixed-Frequency Simulation

The mixed-frequency test used a 1 kHz sine wave combined with a 10 kHz sine wave. The sampling frequency was 100 kHz.

The simulation completed 2,000 samples and generated the waveform file `results/simulation/fir_direct_mixed.vcd`.

## 6. Output Timing and Latency

The output is registered; the testbench reads it right after the clock edge, so y[n] lines up with x[n]. The Pipelined design will add extra delay, so its comparison must shift by its latency.

## 7. Conclusion

The Direct Form FIR passed the recorded impulse-response and reset tests. The Python-versus-Verilog comparison reported zero mismatches and zero maximum absolute error for 2,000 samples.

These results establish functional verification for the tested cases. They do not, by themselves, establish FPGA resource utilization or timing performance.
