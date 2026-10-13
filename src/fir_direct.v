`timescale 1ns/1ps
module fir_direct (
    input wire clk,
    input wire rst,
    input wire signed [15:0] sample_in,
    output reg signed [31:0] sample_out
);

    reg signed [15:0] x1, x2, x3, x4, x5, x6, x7;

    localparam signed [15:0] H0 = 16'sd570;
    localparam signed [15:0] H1 = 16'sd2006;
    localparam signed [15:0] H2 = 16'sd5445;
    localparam signed [15:0] H3 = 16'sd8363;
    localparam signed [15:0] H4 = 16'sd8363;
    localparam signed [15:0] H5 = 16'sd5445;
    localparam signed [15:0] H6 = 16'sd2006;
    localparam signed [15:0] H7 = 16'sd570;

    reg signed [31:0] p0, p1, p2, p3;
    reg signed [31:0] p4, p5, p6, p7;
    reg signed [34:0] accumulator;

    always @(*) begin
        p0 = sample_in * H0;
        p1 = x1 * H1;
        p2 = x2 * H2;
        p3 = x3 * H3;
        p4 = x4 * H4;
        p5 = x5 * H5;
        p6 = x6 * H6;
        p7 = x7 * H7;

        accumulator =
            {{3{p0[31]}}, p0} +
            {{3{p1[31]}}, p1} +
            {{3{p2[31]}}, p2} +
            {{3{p3[31]}}, p3} +
            {{3{p4[31]}}, p4} +
            {{3{p5[31]}}, p5} +
            {{3{p6[31]}}, p6} +
            {{3{p7[31]}}, p7};
    end

    always @(posedge clk) begin
        if (rst) begin
            x1 <= 16'sd0;
            x2 <= 16'sd0;
            x3 <= 16'sd0;
            x4 <= 16'sd0;
            x5 <= 16'sd0;
            x6 <= 16'sd0;
            x7 <= 16'sd0;
            sample_out <= 32'sd0;
        end else begin
            sample_out <= accumulator[31:0];

            x7 <= x6;
            x6 <= x5;
            x5 <= x4;
            x4 <= x3;
            x3 <= x2;
            x2 <= x1;
            x1 <= sample_in;
        end
    end

endmodule
