#pragma once

typedef struct {
    float b0, b1, b2;
    float a1, a2;
    float x1, x2;
    float y1, y2;
} biquad_t;

void biquad_init_default(void);
float biquad_process(float x);
void biquad_reset(void);
