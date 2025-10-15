# Simulation Report — 3-Way Loudspeaker Design

## 1. Objective
This document presents the **simulation and crossover design** results for the 3-way loudspeaker project.  
All simulations were performed using **VituixCAD**, with individual driver responses imported from manufacturer data and adjusted for real baffle placement and diffraction.

The goal is to achieve a **flat, coherent, and phase-aligned frequency response** within the design constraints.

---

## 2. Simulation Setup

| Parameter | Value / Description |
|------------|---------------------|
| **Software** | VituixCAD2|
| **Drivers used** | Woofer: [__model__], Midrange: [__model__], Tweeter: [__model__] |
| **Baffle dimensions** | Width: [__cm__], Height: [__cm__], Driver spacing: [__cm__] |
| **Listening axis** | [__e.g., tweeter axis__] |
| **Crossover topology** | [__e.g., 3-way Linkwitz-Riley 4th order__] |
| **Target SPL reference** | 2.83 V / 1 m |
| **Simulation distance** | [__m__] |
| **Smoothing** | [__1/12 octave, none, etc.__] |

---

## 3. Frequency Response Simulation

### 3.1 On-Axis Response
- Objective: flat response between **40 Hz and 18 kHz** within ±2 dB.  
- Observation:  
  - Low-frequency roll-off at **≈ [__Hz__]**.  
  - Small dip around **[__Hz__]** due to crossover interaction.  
  - Smooth high-frequency roll-off above **[__Hz__]**.

📈 *(Insert your VituixCAD on-axis SPL plot here)*  
![On-axis frequency response](./frequency_response_plots/on_axis_response.png)

> *Comment:*  
> The simulated on-axis response shows good tonal balance with minimal crossover ripple (<1.5 dB).  
> Further optimization could refine the midrange-tweeter transition near [__Hz__].

---

### 3.2 Off-Axis Response (0°–30°–60°)
- Objective: maintain controlled directivity with smooth off-axis decay.  
- Observation:  
  - Consistent tonal balance up to 30°.  
  - Expected HF attenuation beyond 60° due to tweeter directivity.

📈 *(Insert your off-axis family plot here)*  
![Off-axis response](./frequency_response_plots/off_axis_response.png)

> *Comment:*  
> Off-axis behavior remains smooth, ensuring good spatial coherence and stereo imaging.  
> Minor lobing observed near crossover frequency [__Hz__].

---

## 4. Crossover Network

### 4.1 Design Overview
| Band | Filter Type | Slope | Target Fc | Components |
|-------|--------------|--------|-------------|-------------|
| **Woofer → Midrange** | [__Butterworth / LR__] | [__dB/oct__] | [__Hz__] | [__C, L, R__ values__] |
| **Midrange → Tweeter** | [__Butterworth / LR__] | [__dB/oct__] | [__Hz__] | [__C, L, R__ values__] |

📘 *(Insert screenshot of your crossover network diagram here)*  
![Crossover schematic](./filters/crossover_schematic.png)

> *Comment:*  
> The crossover maintains proper phase alignment between bands with minimal overlap distortion.  
> Level-matching resistors were used to equalize SPL between drivers.

---

### 4.2 Phase Response
📈 *(Insert phase plot here)*  
![Phase response](./frequency_response_plots/phase_response.png)

> *Observation:*  
> Drivers are phase-aligned around crossover frequencies, resulting in coherent summation.  
> Group delay remains acceptable (<10 ms across the band).

---

## 5. Impedance Simulation

| Parameter | Value |
|------------|--------|
| **Nominal impedance** | [__Ω__] |
| **Minimum impedance** | [__Ω__ at __Hz__] |
| **Peak (bass resonance)** | [__Hz__] |

📈 *(Insert impedance curve here)*  
![Impedance curve](./frequency_response_plots/impedance_curve.png)

> *Comment:*  
> The simulated impedance remains amplifier-friendly, never dropping below [__Ω__].  
> The port tuning peak confirms an Fb ≈ [__Hz__], matching the enclosure design.

---

## 6. Power and Directivity

### 6.1 Power Response
📈 *(Insert power response plot)*  
![Power response](./frequency_response_plots/power_response.png)

> *Comment:*  
> The power response follows the on-axis trend with gradual HF roll-off, indicating balanced energy distribution in the room.

### 6.2 Directivity Index (DI)
📈 *(Insert DI plot)*  
![Directivity Index](./frequency_response_plots/directivity_index.png)

> *Comment:*  
> The DI curve is smooth, suggesting consistent radiation and minimal beaming.

---

## 7. Summary of Results

| Criterion | Target | Achieved | Comment |
|------------|---------|-----------|----------|
| **Frequency range** | 40 Hz – 18 kHz | [__Hz range__] | Within ±2 dB |
| **Crossover behavior** | Phase coherent | ✅ | Good alignment |
| **Directivity** | Smooth | ✅ | Balanced off-axis |
| **Impedance** | ≥ 4 Ω | ✅ | Stable |
| **SPL Sensitivity** | 86–88 dB | [__dB__] | Acceptable |
| **Low-frequency cutoff** | 45 Hz | [__Hz__] | Matches design |

---

## 8. Next Steps

- [ ] Validate simulated SPL and phase through **REW measurements**.  
- [ ] Fine-tune crossover component values to minimize on-axis ripple.  
- [ ] Compare measured vs simulated impedance.  
- [ ] Document final tuning adjustments.

---

> _“Simulation is only the first step — measurement makes the design real.”_
