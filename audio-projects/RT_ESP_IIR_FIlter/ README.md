
# ESP32 Audio Loopback with IIR Filter and Switch Control

**Goal:** Implement and demonstrate a real-time **IIR (Infinite Impulse Response)** audio filter on an ESP32 microcontroller using the I²S interface.  
- **Language:** C (ESP-IDF)  
- **Key concepts:** digital filtering, real-time audio pipeline, I²S audio interface  
- **Hardware:** NMP441 microphone + ESP32 +  MAX98357A amplifier + passive speaker   
- **Educational purpose:** understand computational constraints and latency in embedded DSP.

## Overview

This project implements a **real-time audio loopback** on the **ESP32**, with:
- **Microphone input (I²S RX)**
- **Amplifier output (I²S TX)**
- **Optional IIR low-pass filter** (toggleable via a physical button)

It is designed as a **modular and maintainable firmware**, showcasing:
- Real-time audio processing pipeline (16 kHz)
- DSP implementation of a biquad IIR filter (Direct Form I)
- Separation of hardware abstraction (I²S) and DSP logic
- GPIO switch interrupt-based control

This structure makes it a base for embedded audio experiments:
EQs, filters, crossovers, and DSP demonstrations.

---

## Features

- Full-duplex I²S loopback (microphone → amplifier)  
- Configurable **IIR low-pass filter (Butterworth 2ᵉ ordre)**  
- Real-time enable/disable via **GPIO button (BOOT)**  
- Modular design for easy extension  
- ESP-IDF compatible (v5.x)

---

## Project Structure

├── main.c # Application entry point (task creation)  
├── config.h # Global configuration (pins, sampling rate)  
│  
├── i2s_manager.c/.h # I²S RX/TX initialization and configuration  
├── iir_filter.c/.h # Biquad filter implementation (IIR)  
├── switch_control.c/.h # GPIO switch monitoring task  
│  
├── CMakeLists.txt # ESP-IDF component registration  
│  
├── stability.py # Validate filter pole/zero stability  
└── filter.py # Compute and visualize filter frequency response  


### File Responsibilities

| File | Description |
|------|--------------|
| **main.c** | Initializes all modules and runs loopback + control tasks |
| **i2s_manager.c/h** | Sets up I²S RX (microphone) and TX (amplifier) |
| **iir_filter.c/h** | Implements the IIR low-pass filter (biquad, Direct Form I) |
| **switch_control.c/h** | Monitors GPIO button to toggle the filter |
| **config.h** | Contains constants (I²S pins, sample rate, GPIO mapping) |
| **stability.py / filter.py** | Python tools for filter analysis and validation |

---


## Requirements

- ESP-IDF v5.x
- ESP32 board (e.g. ESP32-DevKitC)
- I²S-compatible microphone (e.g. INMP441)
- I²S amplifier or DAC (e.g. MAX98357A)

~~~bash
#Create projet
idf.py create-project "project name"

# Configure target and environment
idf.py set-target esp32

# Build
idf.py build

# Flash to device
idf.py flash

# Monitor serial output
idf.py monitor
~~~

## Filter Details

- Type: **Butterworth low-pass**
- Order: **2ᵉ ordre (biquad)**
- Cutoff frequency: ~100 Hz
- Sampling frequency: 16 kHz
- Implementation: **Direct Form I**
- Coefficients (default in `iir_filter.c`) :

~~~c
b0 = 0.0003751f;
b1 = 0.0007501f;
b2 = 0.0003751f;
a1 = -1.9444777f;
a2 = 0.9459779f;
~~~

## Python Validation (stability & frequency response)

This project includes two small Python utilities to **validate the IIR filter design** and **inspect its response** before flashing the firmware.  
Those files can be found in DSP_tools repository.

### IIR_stability_analyser.py - pole/zero check & stability plot
- Computes zeros/poles from your coefficients
- Verifies stability (all poles strictly inside the unit circle)
- Draws a Z-plane diagram (poles/zeros + unit circle)

### IIR_coef_filer_calculator.py - coefficient "cookbook" + Bode plots
- Provides biquad generator functions (low-pass, high-pass, band-pass, notch, peaking)
- Returns normalized coefficients [b0,b1,b2], [1,a1,a2]
- Plots magnitude (dB) and phase for quick inspection

### dependancies
~~~bash
pip install numpy scipy matplotlib
~~~
## Performance Analysis

The ESP32 implementation achieves **stable real-time audio processing** with an extremely low and consistent latency between the microphone input and the speaker output.

### Processing Load

Real-time performance was measured using `esp_timer_get_time()` around the main processing loop  
(`i2s_channel_read()` → IIR filter → `i2s_channel_write()`).


At 16 kHz and a DMA frame size of **128 samples**:
- Each block represents **8 ms of audio**.  
- The measured processing time of **7.80 ms** means the ESP32 processes each audio block **just within the real-time window**, achieving a near 100 % real-time rate with minimal buffer latency.

### Estimated End-to-End Latency

The total latency of the audio path combines:
- RX DMA buffering (128 samples → 8 ms)  
- Processing (measured ≈ 7.8 ms)  
- TX DMA buffering (128 samples → 8 ms)

**Total estimated latency ≈** 8 + 7.8 + 8 =  23.8 ms

This corresponds to a **real-world latency of ~24 ms**,  
which is **inaudible to the human ear** and comparable to professional-grade low-latency monitoring systems.

### 🔹 Stability

With the configuration  
`dma_frame_num = 128` and `dma_desc_num = 3`:
- The system maintains **continuous audio without underruns or overruns**.  
- Audio propagation feels **instantaneous** during live use.

## Possible Extensiosn
- Add FIR filtering (e.g., convolution EQ)
- Implement multi-band parametric EQ
- Add FFT-based visualization or spectral analysis
- Add IIR filter design function configurable via UART or web interface
- Switch between low-pass / high-pass / bypass
