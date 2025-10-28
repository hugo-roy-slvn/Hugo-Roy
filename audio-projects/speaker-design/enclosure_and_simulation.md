# Enclosure Design & Simulation — 3-Way Loudspeaker Project

## 1. Objective

The goal of this section is to **design and simulate** both the **enclosure geometry** and the **crossover network** to achieve the desired **acoustic balance**, **frequency response**, and **mechanical stability**.

The enclosure design includes a **bass-reflex** configuration for the woofer and **sealed sub-enclosures** for the midrange and tweeter.  
The crossover network is **simulated and optimized in VituixCAD** to ensure smooth driver integration, accurate phase alignment, and a natural tonal balance.

## 2. General Enclosure Concept

| Band | Type | Purpose |
|------|------|----------|
| **Woofer** | Bass-reflex (ported) | Extend low-frequency response and reduce cone excursion. |
| **Midrange** | Sealed sub-enclosure | Isolate from woofer pressure and stabilize the midband. |
| **Tweeter** | Closed back / integrated | Natural mechanical damping of dome driver. |

---

## 3. Design Parameters

### 3.1 Woofer Enclosure

| Parameter | Symbol | Target / Measured | Unit |
|------------|---------|-------------------|------|
| Equivalent compliance volume | \( V \) | [__39__] | L |
| Resonance frequency | \( f_s \) | [_33_Hz__] | Hz |
| Total Q factor | \( Q \) | [4,9] | – |
| Enclosure internal volume | \( V_b \) | [_42__] | L |


### 3.2 Midrange Sub-Enclosure

| Parameter | Target Value | Comment |
|------------|---------------|----------|
| Internal volume | [_5_L__] | Minimized to prevent LF resonance. |
| Wall damping | polyester wool | Reduces internal reflections. |
| Isolation | ✅ Separate from woofer chamber | Prevents pressure modulation. |
| Resonant frequency | > [_85_Hz__] |  |
| Enclosure internal volume | \( V_b \) | [5] L  |  |



### 3.3 Port (Bass Reflex Vent) & Box Design 

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

The simulated SPL response shows a dip around 50 Hz, which is expected to be compensated by the contribution of the bass reflex port. The impedance curve remains satisfactory, consistently above 5 Ω. Phase alignment was challenging to fine-tune, so it was left as currently modeled, with the final evaluation to be performed through listening tests.

## 7. Summary and Next Steps

| Next Step | Description |
|------------|--------------|
| 🔹 Measure frequency response with REW | Validate simulated  response. |
| 🔹 Adjust damping and port tuning | Refine transient balance and reduce resonance. |



