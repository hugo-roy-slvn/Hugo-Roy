# 🔊 3-Way Loudspeaker Design
<img width="241" height="606" alt="image" src="https://github.com/user-attachments/assets/24191ee2-f12e-46c2-aa37-899eb7c8abb9" />

This project presents the design and acoustic simulation of a **high-fidelity 3-way passive loudspeaker**.  
The goal is to develop a system capable of **accurate, linear, and detailed sound reproduction**,  
while deepening my understanding of **electroacoustic design** and **filter interaction**.

## Objectives
- Design a **3-way passive speaker** with balanced frequency response and coherent phase.  
- Learn and apply **simulation methods (VituixCAD)** for system-level design.  
- Perform **measurements with REW** to validate simulation results.  
- Bridge **electrical filter theory**, **acoustics**, and **subjective perception**.

## Design Overview
| Subsystem | Description |
|------------|--------------|
| **Woofer** | Handles low frequencies (30–500 Hz), optimized enclosure volume and port tuning. |
| **Midrange** | Covers 500–3000 Hz, designed for minimal distortion and natural vocal tone. |
| **Tweeter** | Reproduces high frequencies (3–20 kHz), high sensitivity and smooth response. |
| **Crossover** | 3-way passive crossover simulated in VituixCAD. |

## Workflow
1. **Specification phase:** define SPL target, frequency range, and acoustic goals.  
2. **Simulation phase:** import drivers and simulate crossover using *VituixCAD*.  
3. **Enclosure design:** CAD modeling and volume calculation.  
4. **Measurement phase:** REW analysis (magnitude, phase, impedance). (in progress)
 
## Tools & Software
- **VituixCAD** — Electrical and acoustic simulation  
- **REW (Room EQ Wizard)** — Frequency response & impedance measurements  
- **Fusion360** — Enclosure and mechanical design  

## Project Files
- `target_requirements/` → design targets and sketches   
- `enclosure_and_simulation/` → material selection, design notes & VituixCAD
- `measurements/` → REW measurement data and analysis (in progress)
- `results_and_discussion/` → comparison and final evaluation (in progres)

## Learning Outcomes
- Improved understanding of **frequency-domain modeling** and **filter acoustics**.  
- Experience with **measurement calibration** and **room influence** mitigation.  
- Practical knowledge in **loudspeaker system integration** (drivers + enclosure + crossover).  



> _“Designing a loudspeaker is where theory meets the art of listening.”_ 🎶
