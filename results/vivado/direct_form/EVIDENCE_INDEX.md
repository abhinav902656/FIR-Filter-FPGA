# Direct Form Vivado Evidence Index

## Publication evidence

Sanitized publication copies are stored in `results/vivado/direct_form_sanitized/`. The files below are relative to that directory. Original reports and logs remain in `results/vivado/direct_form/` and the local raw archive. Do not publish the raw archive or local checkpoints.

| Publication file | What it shows | Source flow | Sanitized copy |
|---|---|---|---|
| `synth_timing.rpt` | Synthesis timing summary | Batch Tcl | Yes |
| `synth_utilization.rpt` | Synthesis resource use | Batch Tcl | Yes |
| `impl_clock.rpt` | Clock report | Batch Tcl | Yes |
| `impl_drc.rpt` | Implementation DRC findings | Batch Tcl | Yes |
| `impl_power.rpt` | Implementation power estimate | Batch Tcl | Yes |
| `impl_timing.rpt` | Implementation timing summary | Batch Tcl | Yes |
| `impl_utilization.rpt` | Implementation resource use | Batch Tcl | Yes |
| `gui_drc.rpt` | DRC findings from routed checkpoint | GUI checkpoint | Yes |
| `gui_power.rpt` | Power estimate from routed checkpoint | GUI checkpoint | Yes |
| `gui_timing_summary.rpt` | Routed timing summary | GUI checkpoint | Yes |
| `gui_utilization.rpt` | Routed resource use | GUI checkpoint | Yes |
| `gui_utilization_hier.rpt` | Hierarchical resource use | GUI checkpoint | Yes |
| `gui_worst_input_path.rpt` | Worst input path report | GUI checkpoint | Yes |
| `gui_worst_paths.rpt` | Detailed worst-path report | GUI checkpoint | Yes |
| `dsp_config.txt` | DSP48E1 register settings | Evidence extraction | Yes |
| `run_info.txt` | Tool, part, target, and flow notes | Written after runs | Yes |
| `vivado_run_console.txt` | Batch run messages and timing summaries | Batch Tcl | Yes |
| `SANITIZATION_NOTE.txt` | Sanitization procedure and scope | Documentation | Yes |

The GUI reports were produced by opening the routed checkpoint. They are not presented as reports from the batch flow.

## Local-only evidence

These files remain in `results/vivado/direct_form/` and are not included in the sanitized publication set.

| Original file | Purpose | Publication status |
|---|---|---|
| `vivado_run_journal.txt` | Local Vivado journal | Do not publish |
| `fir_direct_synth.dcp` | Synthesis checkpoint | Binary; local only |
| `fir_direct_routed.dcp` | Routed checkpoint | Binary; local only |
| `EVIDENCE_INDEX.md` | This index | Publication documentation |

Original evidence is also preserved in the ignored `results/vivado/direct_form_raw/` archive. Keep the original hashes and sanitization verification output with the local project records. The timing summaries from the batch console and routed GUI report must remain clearly distinguished.