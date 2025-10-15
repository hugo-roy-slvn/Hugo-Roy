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
| Equivalent compliance volume | \( V_\text{as} \) | [__L__] | L |
| Resonance frequency | \( f_s \) | [__Hz__] | Hz |
| Total Q factor | \( Q_\text{ts} \) | [__value__] | – |
| Desired alignment | – | [__Butterworth / QB3 / Custom__] | – |
| Enclosure internal volume | \( V_b \) | [__L__] | L |
| Tuning frequency | \( f_b \) | [__Hz__] | Hz |
| Target -3dB cutoff | \( f_3 \) | [__Hz__] | Hz |

📈 *(Insert your VituixCAD or WinISD bass response simulation)*  
![Bass reflex tuning](./renders/bass_reflex_tuning.png)

> *Comment:*  
> The bass reflex alignment provides a -3 dB cutoff at **[__Hz__]**,  
> offering a balance between low-frequency extension and transient accuracy.

---

### 3.2 Midrange Sub-Enclosure

| Parameter | Target Value | Comment |
|------------|---------------|----------|
| Internal volume | [__L__] | Minimized to prevent LF resonance. |
| Wall damping | [__Material: e.g., acoustic foam 20 mm__] | Reduces internal reflections. |
| Isolation | ✅ Separate from woofer chamber | Prevents pressure modulation. |
| Resonant frequency | > [__Hz__] | Above crossover region. |

📘 *(Insert schematic of midrange sub-chamber)*  
![Midrange chamber diagram](./renders/midrange_chamber.png)

> *Comment:*  
> The sub-enclosure volume ensures minimal interaction with woofer pressure while maintaining smooth midrange response.

---

### 3.3 Port (Bass Reflex Vent) Design

| Parameter | Symbol | Target / Measured | Unit |
|------------|---------|-------------------|------|
| Tuning frequency | \( f_b \) | [__Hz__] | Hz |
| Port type | – | [__circular / slot / rear / front__] | – |
| Port diameter | \( D_p \) | [__mm__] | mm |
| Port length | \( L_p \) | [__mm__] | mm |
| Air velocity (max) | \( v_{max} \) | [__m/s__] | m/s |
| Resonance suppression | – | [__e.g., flared edges, damping near vent__] | – |

📈 *(Insert simulation graph of port air velocity or tuning response)*  
![Bass reflex tuning](./renders/port_tuning.png)

> *Comment:*  
> The port is tuned to **[__Hz__]**, providing an F₃ around **[__Hz__]**.  
> A flared edge minimizes turbulence and port noise, ensuring clean bass even at high SPL.  
> Simulated maximum air velocity remains below **17 m/s** at nominal listening level.

#### Port Placement and Acoustic Impact

- **Location:** [__front / rear / bottom__]  
- **Distance from walls:** ≥ [__cm__]  
- **Impact:** Front ports simplify placement near walls, while rear ports may improve LF extension in free-field setups.  
- **Simulation result:** Smooth response with minimal port-induced phase shift around \( f_b \).

📸 *(Optional: include a photo or 3D render of the port placement)*  
![Port location](./renders/port_location.png)

---

## 4. Construction Details

| Element | Material | Dimensions / Notes |
|----------|-----------|--------------------|
| **Panels** | MDF or birch plywood | [__thickness__] mm |
| **Front baffle** | MDF double layer | Improves rigidity and reduces resonance. |
| **Bracing** | Internal cross-braces | Reduces panel vibration. |
| **Damping material** | [__e.g., polyester wool / bitumen / foam__] | Applied to side and back walls. |
| **Finish** | [__paint / veneer / raw prototype__] | Aesthetic choice. |

📸 *(Insert internal bracing photo or 3D drawing)*  
![Internal bracing](./renders/bracing_diagram.png)

> *Comment:*  
> Proper bracing and damping ensure low mechanical coloration and consistent midbass clarity.

---

## 5. Baffle Layout and Driver Placement

| Driver | Center height (mm) | Spacing | Baffle offset | Notes |
|---------|-------------------|----------|----------------|-------|
| **Tweeter** | [__mm__] | Aligned with ear height (~1.0 m) | [__mm__] | Reference axis |
| **Midrange** | [__mm__] | [__distance to tweeter__] | [__mm__] | Time alignment consideration |
| **Woofer** | [__mm__] | [__distance to midrange__] | [__mm__] | Centered for LF symmetry |

📘 *(Insert your front view layout sketch)*  
![Baffle layout](./renders/baffle_layout.png)

> *Comment:*  
> Vertical driver alignment minimizes lobing and maintains consistent phase summation around crossover frequencies.

---

## 6. Simulation Results

| Test | Result | Comment |
|------|---------|----------|
| **Port tuning frequency (f₍b₎)** | [__Hz__] | Matches target ±5%. |
| **Low-frequency -3 dB point (f₍3₎)** | [__Hz__] | Consistent with design. |
| **Group delay** | [__ms__] | Below perceptual threshold in bass. |
| **Cabinet resonance (main mode)** | [__Hz__] | No significant coloration expected. |

📈 *(Insert SPL + impedance plot of woofer in box)*  
![Enclosure simulation](./renders/box_simulation_plot.png)

> *Comment:*  
> The simulated low-end behavior matches expectations. Port and box tuning provide balanced bass without boominess.

---

## 7. Summary and Next Steps

| Next Step | Description |
|------------|--------------|
| 🔹 Build prototype enclosure | Cut and assemble MDF panels according to CAD plan. |
| 🔹 Measure frequency response (nearfield + farfield) | Validate simulated bass response. |
| 🔹 Adjust damping and port tuning | Refine transient balance and reduce resonance. |
| 🔹 Integrate full 3-way crossover | Verify global system response. |

---

> _“A well-designed enclosure is as much an acoustic instrument as it is an engineering structure.”_
