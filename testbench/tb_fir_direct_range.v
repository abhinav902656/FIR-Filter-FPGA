`timescale 1ns/1ps

module tb_fir_direct_range;

    reg clk;
    reg rst;
    reg signed [15:0] sample_in;
    wire signed [31:0] sample_out;

    integer i;
    integer errors;

    reg signed [15:0] test_values [0:3];
    reg signed [31:0] expected_values [0:3];

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
        test_values[0] = 16'sd32767;
        test_values[1] = -16'sd32768;
        test_values[2] = 16'sd0;
        test_values[3] = 16'sd1;

        expected_values[0] = 32'sd18677190;
        expected_values[1] = 32'sd47052842;
        expected_values[2] = 32'sd112683707;
        expected_values[3] = 32'sd95609231;

        errors = 0;
        rst = 1'b1;
        sample_in = 16'sd0;

        repeat (2) @(negedge clk);
        rst = 1'b0;

        for (i = 0; i < 4; i = i + 1) begin
            sample_in = test_values[i];

            @(posedge clk);
            #1;

            if (sample_out !== expected_values[i]) begin
                $display(
                    "FAIL: Input %0d, expected %0d, got %0d",
                    test_values[i], expected_values[i], sample_out
                );
                errors = errors + 1;
            end else begin
                $display(
                    "PASS: Input %0d, output %0d",
                    test_values[i], sample_out
                );
            end

            @(negedge clk);
        end

        if (errors == 0)
            $display("PASS: All full-range tests passed.");
        else
            $display("FAIL: %0d range test(s) failed.", errors);

        $finish;
    end

endmodule
