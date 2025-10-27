# Project Specifications — 3-Way Loudspeaker Design

## 1. Project Overview
This project aims to design and build a **high-fidelity 3-way passive loudspeaker** optimized for **accurate sound reproduction**, **low distortion**, and **balanced tonal response**.

The design follows a **studio-monitor philosophy**, prioritizing linearity, transient accuracy, and natural timbre over sheer SPL (Sound Pressure Level).

---

## 2. Design Objectives

| Category | Target Specification | Rationale |
|-----------|----------------------|------------|
| **Frequency Response** | 50 Hz – 20 kHz (±2 dB) | Achieve full-range reproduction suitable for music and monitoring. |
| **Sensitivity** | ~86–88 dB / 2.83V / 1m | Balanced efficiency for domestic amplification. |
| **Nominal Impedance** | 4 Ω | Standard load compatible with most amplifiers. |
| **Crossover Frequency** | LF–MF: ~500 Hz, MF–HF: ~5000 Hz | Typical 3-way distribution minimizing overlap and distortion. |
| **Power Handling** | 60–80 W RMS | Adequate for medium-sized rooms without driver stress. |
| **Enclosure Type** | Bass-reflex, front-ported | Extend low-frequency response and ease placement. |
| **Directivity** | Smooth off-axis response (±30°) | Maintain tonal balance and stereo imaging. |


---

## 3. Constraints & Design Considerations

| Type | Description |
|------|--------------|
| **Budget** | 300–500 € total (drivers, crossover components, materials). |
| **Form Factor** | Bookshelf-style enclosure (~40–50 L) for practical testing. |
| **Measurement Equipment** | UMIK-1 or XLR microphone + Scarlett Solo interface. |
| **Tools Available** | VituixCAD (simulation), REW (measurements), Fusion360 (CAD). |
| **Amplification** | Passive crossover; external stereo amplifier for testing. |

---

## 4. Driver Selection (Preliminary)

| Band | Model (Example) | Key Specs | Role |
|------|------------------|------------|------|
| **Woofer** | SB Acoustics SB17MFC35-8 | Fs ≃ 33 Hz, Qts ≃ 0.37, SPL ≃ 88 dB | Low-frequency range & foundation. |
| **Midrange** | Monacor MSH-115 | Smooth response 300–5000 Hz | Vocal range & definition. |
| **Tweeter** | Audax TW025A0 | Fs ≃ 1000 Hz, low distortion | High-frequency detail and clarity. |

---

## 5. Performance Goals

- Flat **on-axis frequency response** with controlled crossover summation.
- **Phase-coherent** transition between drivers.
- Optimized **baffle geometry** to reduce diffraction effects.
- **Vent tuning** to achieve ~50 Hz f₃ cutoff.
- Realistic **group delay** (<15 ms in bass region).
- Maintain **acoustic center alignment** between drivers for coherent imaging.

---

## 6. Simulation Targets

Using **VituixCAD**, the following analyses will be conducted:
- **Frequency and phase response** (on axis).  
- **Crossover optimization** (component tuning).  
- **Impedance simulation** for amplifier compatibility.  

Each simulation step will be documented and compared to measurement data once available.

---
