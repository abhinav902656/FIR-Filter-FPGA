
`timescale 1ns/1ps

module tb_fir_direct;

    reg clk;
    reg rst;
    reg signed [15:0] sample_in;
    wire signed [31:0] sample_out;

    integer i;

    fir_direct dut (
        .clk(clk),
        .rst(rst),
        .sample_in(sample_in),
        .sample_out(sample_out)
    );

    // 100 MHz simulation clock
    initial begin
        clk = 1'b0;
        forever #5 clk = ~clk;
    end

    initial begin
        $dumpfile("results/simulation/fir_direct.vcd");
        $dumpvars(0, tb_fir_direct);

        rst = 1'b1;
        sample_in = 16'sd0;

        // Apply synchronous reset.
        repeat (2) @(negedge clk);
        rst = 1'b0;

        // Apply an impulse followed by seven zero samples.
        sample_in = 16'sd32767;

        for (i = 0; i < 8; i = i + 1) begin
            @(negedge clk);
            sample_in = 16'sd0;
        end

        // Allow the final result to be observed.
        repeat (2) @(negedge clk);

        $display("Impulse response test completed.");
        $finish;
    end

    always @(posedge clk) begin
        #1;
        if (!rst) begin
            $display(
                "Time=%0t ns, input=%0d, output=%0d",
                $time, sample_in, sample_out
            );
        end
    end

endmodule
