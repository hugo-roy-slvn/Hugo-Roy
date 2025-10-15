
---

## 🧩 Main Topics Covered

| Area | Description | Key Functions / Files |
|------|--------------|-----------------------|
| **Filtering** | Design and compare FIR vs IIR filters. Explore stability, impulse responses, and spectral effects. | `biquad_lowpass()`, `filter_response_plot.py` |
| **Time-Frequency Analysis** | Compute STFT, energy envelopes, and visualize spectrograms for musical signals. | `compute_stft.py`, `energy_envelope_extraction.py` |
| **Onset Detection** | Implement a simple ODF (Onset Detection Function) using energy and half-wave rectification. | `compute_odf.py` |
| **Sinusoidal Modeling** | Estimate and track sinusoidal components in synthetic and real signals. | `freq_estimation_error.py`, `chirp_tracking.py` |
| **Harmonic Modeling** | Detect harmonic partials, measure inharmonicity, and segment stable frequency regions. | `inharmonicity_measurement.py`, `segment_stable_frequency_regions()` |

---

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

### 🎚️ Harmonic + Stochastic Modeling of Speech
![hps_model](./examples/hps_model_speech.png)

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

