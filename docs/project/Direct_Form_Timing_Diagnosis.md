# Direct Form Timing Diagnosis



## 1. Purpose



This note records the timing problem found in the Direct Form FIR filter.



It will help us understand the problem later without repeating the same investigation. It also records which facts are confirmed and which questions still need answers.



The Direct Form RTL has not been changed as part of this diagnosis.



## 2. Design Setup



- Project: FPGA Implementation of Optimized FIR Filter for Signal Processing

- Architecture: Direct Form FIR

- FPGA part: `xc7a35tcpg236-1`

- Tool: Vivado 2023.2

- Clock period: 10.000 ns

- Timing target: 100 MHz

- Implementation status: Routed

- Board testing: Not performed

- Bitstream: Not generated



The reported results come from Vivado reports. They are not measurements from a physical FPGA board.



## 3. Confirmed Timing Results



The main timing report is `gui_timing_summary.rpt`. The detailed critical-path report is `gui_worst_paths.rpt`.



- Setup WNS: **-0.232 ns**

- Setup TNS: **-0.996 ns**

- Failing setup endpoints: **8 out of 283**

- Hold slack: **+0.080 ns**

- Hold failures: **0**

- Pulse-width slack: **+4.500 ns**



The setup timing target is not met. A negative WNS means that the worst setup path misses the required timing by 0.232 ns.



The positive hold slack means that the reported hold checks pass. It does not fix the setup timing problem.



## 4. Critical Path Details



The worst setup path is reported as:



- Start point: `sample_out5/CLK`

- End point: `sample_out_reg[29]/D`

- Required time: 10.000 ns

- Data-path delay: 10.250 ns

- Logic delay: 6.920 ns

- Routing delay: 3.330 ns

- DSP48E1 clock-to-output increment: 4.009 ns

- Logic stages: eight CARRY4 stages and three LUT stages



This path starts at a DSP48E1 clock pin and ends at an output register input. The DSP output and the logic after it are important areas to inspect.



The report shows that both logic and routing contribute to the delay. We should not assume that only one part is responsible.



## 5. DSP Register Settings



The file `dsp_config.txt` reports these settings for the eight DSP48E1 instances:



- `MREG=0` for all eight instances.

- `PREG=0` for all eight instances.

- `BREG=0` for all eight instances.

- `AREG` varies between 0, 1, and 2.



`MREG` is the multiplier pipeline register setting. `PREG` is the output pipeline register setting. A value of 0 means that the corresponding register is not enabled in that DSP instance.



These settings are confirmed by the report. Their exact effect on the full critical path has not been tested.



Adding or changing pipeline stages may affect latency, resource use, and output alignment. Do not change the Direct Form RTL based only on these settings.



## 6. Input Path Check



The report `gui_worst_input_path.rpt` shows:



- Start point: `sample_in[1]`

- End point: `sample_out_reg[29]/D`

- Slack: `+1.158 ns`

- Data-path delay: `13.192 ns`

- Logic delay: `7.583 ns`

- Routing delay: `5.609 ns`

- Logic stages: 13



The input and output delays are both set to 0 ns in this run. Therefore, this path must be interpreted using the current timing constraints. It is not enough to conclude that the design will meet timing with real external input and output devices.



## 7. Possible Causes



The following are investigation points, not proven root causes.



### A. DSP pipeline registers



The DSP report shows that `MREG` and `PREG` are disabled. This may contribute to the delay through the arithmetic path. An alternative implementation has not been tested.



### B. Carry-chain and LUT logic



The critical path contains eight CARRY4 stages and three LUT stages. This shows that logic after the DSP output also contributes to the path delay.



### C. Routing delay



The critical path has 3.330 ns of routing delay. Placement and routing affect timing, so the logic delay alone does not explain the complete result.



### D. Register distribution



The routed design reports 32 registers. The reason for this count has not been fully established. The hierarchical utilization report and mapped logic need further review before drawing a conclusion.



## 8. Resource and Power Results



The routed utilization report shows:



- LUTs: 204 out of 20,800

- Registers: 32 out of 41,600

- DSP48E1: 8 out of 90

- BRAM: 0 out of 50

- Bonded I/O: 50 out of 106

- BUFGCTRL: 1 out of 32



The power report shows:



- Total estimated on-chip power: 0.116 W

- Estimated dynamic power: 0.046 W

- Estimated static power: 0.070 W

- Estimated junction temperature: 25.6 degrees C

- Confidence: Low



These are tool estimates. Power was not measured on a physical board. The report uses a vectorless estimate, so the values should not be treated as final hardware power results.



## 9. Design Rule Check Findings



The report `gui_drc.rpt` contains 20 findings:



- `NSTD-1`: 1 Critical Warning

- `UCIO-1`: 1 Critical Warning

- `CFGBVS-1`: 1 Warning

- `DPIP-1`: 1 Warning

- `DPOP-1`: 8 Warnings

- `DPOP-2`: 8 Warnings



The reports also show that all 50 ports use the default I/O standard and all 50 ports lack pin locations. The configuration voltage settings are also missing.



The physical board and its pin assignments have not been confirmed. Do not guess pin locations or voltage settings, and do not hide these findings just to make the report look clean.



The design is not ready for bitstream generation until the board constraints and relevant warnings have been properly reviewed.



## 10. Unresolved Questions



- The batch console contains timing summaries showing WNS -0.268 ns and TNS -1.350 ns (console lines 879 and 958).

- The reason for the reported register count has not been fully established.

- The detailed cause of every DSP pipelining warning has not been independently verified.

- The final effect of enabling DSP pipeline registers has not been tested.

- The input and output timing constraints need review before making claims about real external timing.

- The physical-board pin and voltage constraints remain unconfirmed.



The routed GUI timing summary reports WNS -0.232 ns and TNS -0.996 ns. The exact relationship between the console summaries and the routed GUI summary has not been established. Keep the values labelled by source; do not average them or combine them into one result.



## 11. What to Check in Future



Before changing the design, follow this order:



1. Confirm the FPGA part and clock period.

2. Confirm that the timing report belongs to the latest intended routed run.

3. Check WNS, TNS, failing endpoints, and hold slack.

4. Open the detailed worst-path report and identify the start point, end point, logic delay, and routing delay.

5. Check DSP register settings and the mapped logic.

6. Compare the utilization and DRC reports with the recorded values in this note.

7. Identify whether a proposed change affects arithmetic accuracy, latency, output alignment, or resource use.

8. Make a change only after its purpose and expected effect are clear.

9. If a future run produces different results, record its report date and keep the old evidence until the difference is explained.

10. Re-run the required simulation and implementation checks only when explicitly approved in the project workflow.



Do not change RTL, XDC constraints, or implementation settings simply to remove a warning or improve one number. Any change must preserve the fixed filter requirements and be verified with evidence.



## 12. Conclusion



The Direct Form FIR design does not meet the 10 ns setup timing target. Its routed WNS is -0.232 ns, and eight of 283 setup endpoints fail.



The critical path includes a DSP48E1 clock-to-output delay, carry-chain logic, LUT logic, and routing delay. These reports identify useful areas for future investigation, but they do not prove one single root cause.



The Direct Form RTL remains unchanged. No implementation rerun or physical-board test was performed as part of this diagnosis.



DSP pipeline architecture changes must be handled separately and must not be mixed into this Direct Form diagnosis.

**Result:** Timing not met at the 10 ns target (WNS -0.232 ns).
