# Output Scaling Decision — FIR Architectures

## 1. Purpose

This document records the output-scaling decision for the project
"FPGA Implementation of Optimized FIR Filter for Signal Processing".

It explains the decision so that team members, the project guide,
and reviewers can understand and verify it later.

## 2. Fixed Project Specifications

- Filter: 8-tap Hamming low-pass FIR
- Sampling frequency: 100 kHz
- Cutoff frequency: 5 kHz
- Input: signed 16-bit Q15
- Output: signed 32-bit
- Implementation: Verilog
- Coefficients: quantized Q15 integers generated using SciPy

These specifications are not changed by this decision.

## 3. Decision

The four architectures will use the same raw coefficient-product sum:

1. Direct Form: fir_direct.v
2. Pipelined: fir_pipelined.v
3. Symmetric: fir_symmetric.v
4. Combined: fir_combined.v

The output is not shifted back to Q15 in the current design.

All architectures must use the same coefficient values, input
interpretation, output scaling, and reference-model convention.
This allows a fair numerical comparison.

## 4. Coefficients

The current Q15 integer coefficients are:

570, 2006, 5445, 8363, 8363, 5445, 2006, 570

Their sum is 32768. All coefficients are positive and symmetric.

## 5. Numerical Meaning

Let x_int[n] be the signed integer representing the Q15 input,
and let h_int[k] be the signed integer representing a Q15 coefficient.

The current output is:

y_raw[n] = sum from k=0 to 7 of
           x_int[n-k] * h_int[k]

The integer products have a Q30 fractional scale because
Q15 multiplied by Q15 gives Q30.

The output is therefore a raw product-sum, not a normalized Q15 sample.
The output port stores this integer sum in a signed 32-bit signal.

## 6. Numeric-Range Verification

For the current coefficients:

sum(abs(h_int[k])) = 32768

The maximum positive input integer is 32767.
The minimum negative input integer is -32768.

A conservative bound on the output is:

Maximum positive bound:
32767 * 32768 = 1,073,709,056

Maximum magnitude for negative input:
32768 * 32768 = 1,073,741,824

The signed 32-bit range is:
-2,147,483,648 to 2,147,483,647

Both bounds fit in signed 32-bit output.

This check assumes the specified input range and the current
positive coefficients. Recalculate the bounds if coefficients
or input width change.

## 7. Python Reference Model

The Python reference must calculate the same raw integer
convolution. It must not shift the output back to Q15 when
comparing against the current Verilog output.

The Direct Form mixed-signal test previously produced 2000
output samples, with zero mismatches against the Python reference.

Repeat the comparison after modifying the RTL or coefficients.

## 8. Important Limitations

- Raw output values must not be interpreted directly as normalized
  Q15 samples.
- Any downstream module must know that the output has Q30 scale.
- A future interface requiring Q15 output would need a defined
  conversion, rounding, and overflow/saturation policy.
- Any such change must be applied consistently to all architectures
  and to the Python reference model.
- The 35-bit internal accumulator and 32-bit output must be reviewed
  again if coefficients, input width, or arithmetic behavior changes.

## 9. Explanation for a Reviewer

"We use signed 16-bit Q15 input samples and Q15 integer
coefficients. Their products have Q30 scale. We retain the raw
coefficient-product sum in a signed 32-bit output instead of
shifting it back to Q15. With our current coefficients, the sum of
the absolute coefficient integers is 32768, so the worst-case
output magnitude fits within signed 32-bit range. All four
architectures will use this same convention so their results can
be compared fairly. The Python reference uses the same raw
integer arithmetic."

## 10. Status

Decision: Keep raw product-sum output for all four architectures.

Numeric-range check: Passes for the current coefficient set and
specified signed 16-bit input range.

Recheck this decision if the coefficient set, input width, output
interface, or required numerical format changes.
