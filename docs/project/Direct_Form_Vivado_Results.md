# Direct Form FIR — Vivado Results

## Design setup

- Project: FPGA Implementation of Optimized FIR Filter for Signal Processing
- Architecture: Direct Form FIR
- Tool: Vivado 2023.2
- FPGA part: `xc7a35tcpg236-1`
- Target clock period: 10.000 ns (100 MHz)
- RTL and XDC changed for this evidence collection: No
- Bitstream generated: No
- Physical-board testing performed: No

## Timing result

**Timing not met at the 10 ns target (WNS -0.232 ns).**

The routed timing summary reports WNS = -0.232 ns and TNS = -0.996 ns, with 8 failing setup endpoints out of 283. The reported hold slack is +0.080 ns, with no hold failures.

The estimated maximum frequency is:

`1000 / (10.000 - (-0.232)) = 97.7 MHz` (approximately).

This is an estimate derived from the reported worst negative slack. It is not a separate timing measurement.

The batch console also contains an estimated timing summary with WNS = -0.268 ns and TNS = -1.350 ns. That is a different summary from the routed GUI timing report. The values must not be averaged. The precise relationship between these summaries remains unresolved.

Sources:
- `results/vivado/direct_form_sanitized/gui_timing_summary.rpt`
- `results/vivado/direct_form_sanitized/gui_worst_paths.rpt`
- `results/vivado/direct_form_sanitized/vivado_run_console.txt`

## Resource utilization

| Resource | Used | Device total | Source |
|---|---:|---:|---|
| LUT | 204 | 20,800 | `gui_utilization.rpt` |
| Registers | 32 | 41,600 | `gui_utilization.rpt` |
| DSP48E1 | 8 | 90 | `gui_utilization.rpt` |
| BRAM | 0 | 50 | `gui_utilization.rpt` |
| Bonded I/O | 50 | 106 | `gui_utilization.rpt` |
| BUFGCTRL | 1 | 32 | `gui_utilization.rpt` |

Source: `results/vivado/direct_form_sanitized/gui_utilization.rpt`

## Power estimate

| Metric | Value | Source |
|---|---:|---|
| Total on-chip power | 0.116 W | `gui_power.rpt` |
| Dynamic power | 0.046 W | `gui_power.rpt` |
| Static power | 0.070 W | `gui_power.rpt` |
| Estimated junction temperature | 25.6 °C | `gui_power.rpt` |
| Confidence | Low | `gui_power.rpt` |

Power is a Vivado estimate, vectorless, low confidence. It is not a physical measurement.

## DSP configuration

The DSP configuration evidence reports eight DSP48E1 instances. `MREG=0`, `PREG=0`, and `BREG=0` for all eight instances; `AREG` varies between 0, 1, and 2.

Source: `results/vivado/direct_form_sanitized/dsp_config.txt`

These settings are observations, not proof of a single timing root cause.

## Design-rule findings

The GUI DRC report contains 20 findings: one `NSTD-1` critical warning, one `UCIO-1` critical warning, one `CFGBVS-1` warning, one `DPIP-1` warning, eight `DPOP-1` warnings, and eight `DPOP-2` warnings.

The report identifies missing explicit I/O standards and pin locations, along with configuration-setting issues. Board pin assignments and voltage settings must not be guessed. The current evidence does not establish readiness for bitstream generation.

Source: `results/vivado/direct_form_sanitized/gui_drc.rpt`

## Known limitations

- Input and output delays are both constrained to 0 ns. External interface timing is therefore not fully characterized.
- Power is a vectorless Vivado estimate with low confidence.
- No bitstream was generated, and no physical-board test or hardware measurement was performed.
- Two evidence flows were used: the batch Tcl flow generated the synthesis and implementation reports and console log; opening the routed checkpoint generated the GUI reports.
- `run_info.txt` was written after the flows based on the recorded evidence.
- The difference between the console estimated timing summary and the routed GUI timing summary remains unresolved.
- The physical board's pin assignments and voltage requirements have not been confirmed.
- No claim is made that Direct Form meets timing or that a single root cause has been proven.
- The 10 kHz input component is attenuated, not removed; the recorded gain is approximately 0.66.

## Evidence locations

Sanitized text evidence is in `results/vivado/direct_form_sanitized/`. Original evidence is preserved separately in the local raw archive. The evidence index records the files and their flow.
