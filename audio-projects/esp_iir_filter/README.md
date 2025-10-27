
### ESP32 Audio Loopback with IIR Filter and Switch Control

**Goal:** Implement and demonstrate a real-time **IIR (Infinite Impulse Response)** audio filter on an ESP32 microcontroller using the I²S interface.  
- **Language:** C (ESP-IDF)  
- **Key concepts:** digital filtering, real-time audio pipeline, I²S audio interface  
-  
- **Status:** 🧩 in progress — hardware testing phase  
- **Educational purpose:** understand computational constraints and latency in embedded DSP.

# 🎧 ESP32 Audio Loopback with IIR Filter and Switch Control

## 📘 Overview

This project implements a **real-time audio loopback** on the **ESP32**, with:
- **Microphone input (I²S RX)**
- **Amplifier output (I²S TX)**
- **Optional IIR low-pass filter** (toggleable via a physical button)

It is designed as a **modular and maintainable firmware**, showcasing:
- Real-time audio processing pipeline (16 kHz)
- DSP implementation of a biquad IIR filter (Direct Form I)
- Separation of hardware abstraction (I²S) and DSP logic
- GPIO switch interrupt-based control

This structure makes it an excellent base for embedded audio experiments:
EQs, filters, crossovers, and DSP demonstrations.

---

## ⚙️ Features

✅ Full-duplex I²S loopback (microphone → amplifier)  
✅ Configurable **IIR low-pass filter (Butterworth 2ᵉ ordre)**  
✅ Real-time enable/disable via **GPIO button (BOOT)**  
✅ Modular design for easy extension  
✅ ESP-IDF compatible (v5.x)

---

## 🧱 Project Structure

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

## System Architecture

**Hardware:** INMP441 microphone + ESP32 +  MAX98357A amplifier + Speaker

     ┌──────────────────────────────────────────────┐
     │                 ESP32                        │
     │                                              │
     │   ┌────────┐     ┌────────────┐     ┌──────┐ │
Mic →│   |I²S RX→ │ →→  │ IIR Filter │ →→  │I²S TX│ → Amp → Speaker
     │   | (DMA)  │     │ (optional) │     │(DAC)││ |
     |   └────────┘     └────────────┘     └──────┘ │
     │     GPIO0 Button → Toggle Filter (On/Off)    │
     └──────────────────────────────────────────────┘


## Filter Details

- Type: **Butterworth low-pass**
- Order: **2ᵉ ordre (biquad)**
- Cutoff frequency: ~100 Hz
- Sampling frequency: 16 kHz
- Implementation: **Direct Form I**
- Coefficients (default in `iir_filter.c`) :

```c
b0 = 0.0003751f;
b1 = 0.0007501f;
b2 = 0.0003751f;
a1 = -1.9444777f;
a2 = 0.9459779f;

## Build and Flash Instructions

**Requirements** :
- ESP-IDF v5.x
- ESP3 board
- I²S-compatible microphone (e.g. INMP441)
- I²S amplifier or DAC (e.g. MAX98357A)

# Configure target and environment
idf.py set-target esp32

# Build
idf.py build

# Flash to device
idf.py flash

# Monitor serial output
idf.py monitor
