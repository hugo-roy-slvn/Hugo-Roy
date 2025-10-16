> ⚠️ **Disclaimer:**  
> All of the scripts and analyses in this repository come from exercises of the course *"Digital Signal Processing for Musical Applications" (UPF / MTG)*.  
> None of the implementations presented here claim to be perfect or entirely correct — they are my own answers and learning experiments while studying the course concepts.

## 🧮 Tools & Libraries

These experiments use **Python** and standard scientific libraries:

- `NumPy` — numerical computation  
- `SciPy` — signal processing  
- `Matplotlib` — visualization  
- `librosa` (optional) — audio I/O and spectrogram tools  
- `sms-tools` — sinusoidal and harmonic model implementation (from UPF/MTG course)

---

## 🔬 Example Results

### 🎵 Frequency Tracking of a Chirp
![chirp_tracking](./examples/chirp_tracking.png)

### Segmentation of stable frequency regions of an audio signal
<img width="1974" height="1212" alt="image" src="https://github.com/user-attachments/assets/9319aecf-26ce-4a6a-b47f-bf137340f4b0" />


### 💥 Onset Detection Function (ODF) for Piano Notes
![piano_odf](./examples/piano_odf.png)

---

## 🚀 Learning Goals

Through these mini-projects, I aim to:
- Understand and implement **core DSP blocks** (filters, transforms, models).
- Develop **intuition about frequency-domain behavior** and time-resolution trade-offs.
- Prepare for **embedded implementation** (C/C++ on ESP32 or ARM Cortex-M).
- Build a **solid audio-DSP portfolio** with both theoretical and practical depth.

---

## 🧭 Next Steps

- 🧠 Port selected DSP blocks to **C for ESP32** (real-time processing).
- 🔊 Compare real-time behavior vs. offline simulation.
- 📈 Document performance and audio quality metrics.
- 🗂️ Integrate results into my broader **audio portfolio**.

---

> _This repository reflects my ongoing journey to become a professional Audio DSP Engineer — learning by experimenting, testing, and building._  

