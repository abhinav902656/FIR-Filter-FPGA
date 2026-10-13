
`timescale 1ns/1ps

module tb_fir_direct;

    reg clk;
    reg rst;
    reg signed [15:0] sample_in;
    wire signed [31:0] sample_out;

    integer i;
    integer errors;

    reg signed [31:0] expected [0:7];

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
        $dumpfile("results/simulation/fir_direct.vcd");
        $dumpvars(0, tb_fir_direct);

        expected[0] = 32'sd18677190;
        expected[1] = 32'sd65730602;
        expected[2] = 32'sd178416315;
        expected[3] = 32'sd274030421;
        expected[4] = 32'sd274030421;
        expected[5] = 32'sd178416315;
        expected[6] = 32'sd65730602;
        expected[7] = 32'sd18677190;

        errors = 0;
        rst = 1'b1;
        sample_in = 16'sd0;

        repeat (2) @(negedge clk);

        if (sample_out !== 32'sd0) begin
            $display("FAIL: Output is not zero during reset.");
            errors = errors + 1;
        end

        rst = 1'b0;

        for (i = 0; i < 8; i = i + 1) begin
            if (i == 0)
                sample_in = 16'sd32767;
            else
                sample_in = 16'sd0;

            @(posedge clk);
            #1;

            if (sample_out !== expected[i]) begin
                $display(
                    "FAIL: Tap %0d expected %0d, got %0d",
                    i, expected[i], sample_out
                );
                errors = errors + 1;
            end else begin
                $display(
                    "PASS: Tap %0d output = %0d",
                    i, sample_out
                );
            end

            @(negedge clk);
        end

        sample_in = 16'sd0;
        @(posedge clk);
        #1;

        if (sample_out !== 32'sd0) begin
            $display("FAIL: Output did not return to zero.");
            errors = errors + 1;
        end

        // Assert synchronous reset after nonzero samples.
        rst = 1'b1;
        sample_in = 16'sd0;

        @(posedge clk);
        #1;

        if (sample_out !== 32'sd0) begin
            $display("FAIL: Reset did not clear output.");
            errors = errors + 1;
        end else begin
            $display("PASS: Reset cleared output.");
        end

        // Release reset and check that the delay line was cleared.
        @(negedge clk);
        rst = 1'b0;
        sample_in = 16'sd0;

        @(posedge clk);
        #1;

        if (sample_out !== 32'sd0) begin
            $display("FAIL: Delay line was not cleared by reset.");
            errors = errors + 1;
        end else begin
            $display("PASS: Reset cleared the delay line.");
        end

        if (errors == 0)
            $display("PASS: All Direct Form tests passed.");
        else
            $display("FAIL: %0d test(s) failed.", errors);

        $finish;
    end

endmodule
