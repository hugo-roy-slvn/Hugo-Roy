#include "iir_filter.h"

// Low pass Butterworth 100 Hz @ 16 kHz
static biquad_t filt;

void biquad_init_default(void)
{
    filt.b0 = 0.0003751f;
    filt.b1 = 0.0007501f;
    filt.b2 = 0.0003751f;
    filt.a1 = -1.9444777f;
    filt.a2 = 0.9459779f;
    filt.x1 = filt.x2 = filt.y1 = filt.y2 = 0.0f;
}

float biquad_process(float x)
{
    float y = filt.b0 * x
            + filt.b1 * filt.x1
            + filt.b2 * filt.x2
            - filt.a1 * filt.y1
            - filt.a2 * filt.y2;

    filt.x2 = filt.x1;
    filt.x1 = x;
    filt.y2 = filt.y1;
    filt.y1 = y;

    return y;
}

void biquad_reset(void)
{
    filt.x1 = filt.x2 = filt.y1 = filt.y2 = 0.0f;
}
