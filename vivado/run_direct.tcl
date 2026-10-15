# Project: FPGA Implementation of Optimized FIR Filter for Signal Processing
# Architecture: Direct Form
# Tool: Vivado 2023.2
# Target: xc7a35tcpg236-1
# Bitstream generation is intentionally excluded.

set part_name "xc7a35tcpg236-1"
set top_name "fir_direct"
set out_dir "results/vivado/direct_form"

if {[catch {
    # Create the output directory.
    file mkdir $out_dir

    # Read only the approved RTL and XDC files.
    read_verilog "src/fir_direct.v"
    read_xdc "constraints/vivado/top.xdc"

    # Synthesis.
    synth_design -top $top_name -part $part_name

    report_utilization -file "$out_dir/synth_utilization.rpt"
    report_timing_summary -file "$out_dir/synth_timing.rpt"
    write_checkpoint -force "$out_dir/fir_direct_synth.dcp"

    # Implementation.
    opt_design
    place_design
    route_design

    # Reports after routing.
    report_utilization -file "$out_dir/impl_utilization.rpt"
    report_timing_summary -file "$out_dir/impl_timing.rpt"
    report_power -file "$out_dir/impl_power.rpt"
    report_clock_utilization -file "$out_dir/impl_clock.rpt"
    report_drc -file "$out_dir/impl_drc.rpt"

    # Save the routed design checkpoint.
    write_checkpoint -force "$out_dir/fir_direct_routed.dcp"
} err]} {
    puts stderr "ERROR: Direct Form Vivado flow failed."
    puts stderr $err
    exit 1
}

puts "Direct Form synthesis and implementation flow completed."
puts "No bitstream was generated."
