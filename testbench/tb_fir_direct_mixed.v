
`timescale 1ns/1ps

module tb_fir_direct_mixed;

    reg clk;
    reg rst;
    reg signed [15:0] sample_in;
    wire signed [31:0] sample_out;

    reg signed [15:0] input_samples [0:1999];

    integer i;
    integer infile;
    integer outfile;
    integer read_count;
    integer temp_sample;

    fir_direct dut (
        .clk(clk),
        .rst(rst),
        .sample_in(sample_in),
        .sample_out(sample_out)
    );

    initial begin
        clk = 1'b0;
        forever #5 clk = ~clk;
    end

    initial begin
        $dumpfile("results/simulation/fir_direct_mixed.vcd");
        $dumpvars(0, tb_fir_direct_mixed);

        // Read decimal input samples.
        infile = $fopen("results/mixed_signal_q15.txt", "r");

        if (infile == 0) begin
            $display("FAIL: Could not open input file.");
            $finish;
        end

        for (i = 0; i < 2000; i = i + 1) begin
            read_count = $fscanf(infile, "%d", temp_sample);

            if (read_count != 1) begin
                $display("FAIL: Could not read sample %0d.", i);
                $fclose(infile);
                $finish;
            end

            input_samples[i] = temp_sample;
        end

        $fclose(infile);

        // Open the output file.
        outfile = $fopen(
            "results/simulation/fir_direct_mixed_output.txt", "w"
        );

        if (outfile == 0) begin
            $display("FAIL: Could not open output file.");
            $finish;
        end

        // Apply synchronous reset.
        rst = 1'b1;
        sample_in = 16'sd0;

        repeat (2) @(negedge clk);
        rst = 1'b0;

        // Apply one sample per clock and record the output.
        for (i = 0; i < 2000; i = i + 1) begin
            sample_in = input_samples[i];

            @(posedge clk);
            #1;
            $fdisplay(outfile, "%0d", sample_out);

            @(negedge clk);
        end

        $fclose(outfile);

        $display("Mixed-frequency simulation completed: 2000 samples.");
        $finish;
    end

endmodule
