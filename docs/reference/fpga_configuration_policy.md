# FPGA Configuration Policy

## 1. Purpose

This policy defines how FPGA configuration and architecture-specific FIR filter designs must be managed in the project **FPGA Implementation of Optimized FIR Filter for Signal Processing**.

The project contains four separate FIR architectures:

1. Direct Form — `fir_direct.v`
2. Pipelined — `fir_pipelined.v`
3. Symmetric — `fir_symmetric.v`
4. Combined — `fir_combined.v`

Each architecture must be implemented and evaluated independently.

The current FPGA work is a virtual synthesis and implementation flow using Vivado 2023.2 and the Artix-7 target part `xc7a35tcpg236-1`.

**Physical-board configuration is a separate future task.** The current virtual implementation must not be described as proof of physical-board readiness.

## 2. Separate Common Configuration from Architecture-Specific Design

Common FPGA configuration and architecture-specific RTL must remain separate.

### 2.1 Common FPGA configuration

Common configuration includes:

- Target FPGA part and device settings.
- Clock definitions and timing constraints.
- Input and output delay constraints.
- Synthesis and implementation settings.
- Report-generation scripts.
- Common project documentation and evidence rules.

Reusable configuration should be maintained separately from the RTL implementation of each FIR architecture.

### 2.2 Architecture-specific design

Each architecture must retain its own RTL source and its own verification and implementation results.

- Direct Form: `src/fir_direct.v`
- Pipelined: `src/fir_pipelined.v`
- Symmetric: `src/fir_symmetric.v`
- Combined: `src/fir_combined.v`

Do not mix the implementation concepts of different architectures. Do not change a verified architecture's RTL or configuration as part of another architecture's work without explicit approval.

## 3. Existing XDC and Timing Constraints

The current Vivado constraint file is:

`constraints/vivado/top.xdc`

The existing clock constraint specifies a 10 ns clock period, corresponding to a 100 MHz target clock.

The current input and output delay constraints are set to 0 ns. This limitation must be documented when interpreting timing results.

**Do not change an existing XDC file without explicit approval.**

Do not guess package pins, I/O standards, bank voltages, or other physical-board settings. Do not claim that the constraints are suitable for a physical board unless the actual board requirements have been identified and verified.

Any future constraint changes must be reviewed, documented, and verified against the selected FPGA and board requirements.

## 4. Current Virtual Implementation Status

The current Direct Form implementation has completed synthesis, placement, and routing in Vivado 2023.2.

The routed implementation report recorded:

- Worst negative slack (WNS): -0.232 ns.
- Total negative slack (TNS): -0.996 ns.
- Setup endpoints failing timing: 8.
- Hold timing slack: +0.080 ns.
- LUT usage: 204.
- Register usage: 32.
- DSP48E1 usage: 8.
- Block RAM usage: 0.

The 10 ns clock target was **not met** because the setup timing report contains negative slack.

These results describe the current virtual implementation only. They must not be presented as physical-board measurements.

The power report is a vectorless estimate, not a measurement of actual hardware power.

Report values must be taken from the corresponding generated reports. Do not replace measured report values with estimates or assumed values.

## 5. DRC and Physical-Board Readiness

The current routed design reports I/O-related DRC violations, including:

- `NSTD-1`: I/O ports use the default I/O standard.
- `UCIO-1`: I/O ports do not have package pin assignments.
- `CFGBVS-1`: configuration-bank voltage properties are unspecified.

These findings do not mean that routing failed. However, the current design is not ready for bitstream generation or physical-board programming.

Do not suppress these findings merely to make the report appear clean. Do not invent pin assignments or electrical settings.

Bitstream generation is excluded from the current virtual-only flow.

## 6. Future Physical-Board Configuration

Physical-board configuration must begin only after the actual board and its requirements are confirmed.

Before changing the XDC file or attempting bitstream generation, identify and verify:

1. The exact FPGA development board and FPGA part.
2. The package pin assignments for the clock, reset, input, and output signals.
3. The required I/O standards for the selected pins.
4. The relevant I/O bank voltages and configuration settings.
5. The clock source, frequency, and timing requirements.
6. Any board-specific reset, connector, or interface requirements.
7. The applicable board schematic and official pin-constraint documentation.

Do not assume that the virtual target configuration automatically matches the college board.

The college documentation must refer to the board only as **Xilinx FPGA Development Board (College Provided)** unless more specific identification is authorized and verified.

## 7. DSP and Timing Warnings

DSP-related warnings must be reviewed in context. A warning about internal DSP register pipelining is an optimization finding and must not automatically be treated as a functional failure.

Review timing reports, resource utilization, critical paths, and warning messages separately.

Do not claim that timing passes when WNS is negative or when setup endpoints fail timing.

Any frequency estimate derived from timing slack must be labelled as an estimate and must include its assumptions.

## 8. Reports and Evidence

Each architecture must have its own implementation reports and evidence.

Record actual values for:

- LUT and register utilization.
- DSP and block RAM utilization.
- Setup and hold timing.
- Worst timing path.
- Power estimates and their confidence level.
- DRC findings.
- Latency and functional verification results, where verified.

Keep generated reports distinguishable from screenshots and source files. Do not commit generated checkpoint files (`.dcp`) or temporary Vivado working files unless explicitly approved.

Screenshots must show the relevant Vivado evidence without exposing personal information, credentials, or private paths.

## 9. Change Control

Before changing RTL, XDC constraints, or implementation scripts:

1. Identify the file and the reason for the change.
2. Explain the expected effect.
3. Obtain explicit approval where required by the project rules.
4. Make the smallest necessary change.
5. Run the appropriate verification.
6. Review the generated reports and Git changes before committing.

Do not modify the verified Direct Form RTL without approval. Do not update the README's Vivado results section until the implementation results and evidence have been reviewed and the user explicitly confirms `RESULTS VERIFIED`.

## 10. Policy for All Future Architectures

These rules apply to all four FIR architectures and all future project documentation.

Keep common FPGA configuration separate from architecture-specific RTL. Keep physical-board configuration separate from the current virtual implementation. Never guess board constraints, change an existing XDC without approval, or claim physical-board readiness without verification.