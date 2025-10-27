# Enclosure Design & Simulation — 3-Way Loudspeaker Project

## 1. Objective

The goal of this section is to design and simulate the **enclosure geometry** for each driver (woofer, midrange, tweeter)  
in order to achieve the desired **acoustic alignment**, **low-frequency extension**, and **mechanical stability**.

The design follows a **bass-reflex configuration** for the woofer and **sealed sub-enclosures** for the midrange and tweeter.

---

## 2. General Enclosure Concept

| Band | Type | Purpose |
|------|------|----------|
| **Woofer** | Bass-reflex (ported) | Extend low-frequency response and reduce cone excursion. |
| **Midrange** | Sealed sub-enclosure | Isolate from woofer pressure and stabilize the midband. |
| **Tweeter** | Closed back / integrated | Natural mechanical damping of dome driver. |

📘 *(Insert a 3D rendering or front-view sketch here)*  
![Cabinet Rendering](./renders/cabinet_front.png)

> *Comment:*  
> The cabinet design aims to balance internal volume, stiffness, and diffraction control for accurate imaging.

---

## 3. Design Parameters

### 3.1 Woofer Enclosure

| Parameter | Symbol | Target / Measured | Unit |
|------------|---------|-------------------|------|
| Equivalent compliance volume | \( V_\text{as} \) | [__39__] | L |
| Resonance frequency | \( f_s \) | [_33_Hz__] | Hz |
| Total Q factor | \( Q_\text{ts} \) | [4,9] | – |
| Enclosure internal volume | \( V_b \) | [_50__] | L |

📈 *(Insert your VituixCAD or WinISD bass response simulation)*  
![Bass reflex tuning](./renders/bass_reflex_tuning.png)


### 3.2 Midrange Sub-Enclosure

| Parameter | Target Value | Comment |
|------------|---------------|----------|
| Internal volume | [_5_L__] | Minimized to prevent LF resonance. |
| Wall damping | polyester wool | Reduces internal reflections. |
| Isolation | ✅ Separate from woofer chamber | Prevents pressure modulation. |
| Resonant frequency | > [_85_Hz__] |  |

📘 *(Insert schematic of midrange sub-chamber)*  
![Midrange chamber diagram](./renders/midrange_chamber.png)


### 3.3 Port (Bass Reflex Vent) Design

<img width="900" height="347" alt="image" src="https://github.com/user-attachments/assets/83e5223b-7520-4b92-9d2e-6e73fd28355b" />


## 4. Construction Details

| Element | Material | Dimensions / Notes |
|----------|-----------|--------------------|
| **Panels** | plywood | 18 mm |
| **Front baffle** | plywood | 15mm |
| **Bracing** | Internal cross-braces | Reduces panel vibration. |
| **Damping material** | polyester wool + foam| Applied to side and back walls. |
| **Finish** | veneer | Aesthetic choice. |

<img width="241" height="606" alt="image" src="https://github.com/user-attachments/assets/6220ba01-7b56-497f-80ae-bdbd4cf36b53" />

## Crossover topology 
<img width="654" height="513" alt="image" src="https://github.com/user-attachments/assets/df46806c-ce6b-4e18-b71f-693db98a815d" />

## 6. Simulation Results

<img width="560" height="519" alt="image" src="https://github.com/user-attachments/assets/28838a82-7237-422a-9f87-964ce7d46e42" />


## 7. Summary and Next Steps

| Next Step | Description |
|------------|--------------|
| 🔹 Build prototype enclosure | Cut and assemble MDF panels according to CAD plan. |
| 🔹 Measure frequency response (nearfield + farfield) | Validate simulated bass response. |
| 🔹 Adjust damping and port tuning | Refine transient balance and reduce resonance. |



