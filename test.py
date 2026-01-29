import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 1. Filter Parameters
fs = 1000  # Sampling frequency
f_l = 0.5  # High-pass cutoff (Baseline wander)
f_h = 150  # Low-pass cutoff (High freq noise)
f_notch = 50.0  # Power-line interference
Q = 30.0  # Quality factor for notch

# 2. Create Butterworth Band-pass
b_band, a_band = signal.butter(4, [f_l, f_h], btype='bandpass', fs=fs)
w_band, h_band = signal.freqz(b_band, a_band, worN=8000, fs=fs)

# 3. Create Digital Notch Filter
b_notch, a_notch = signal.iirnotch(f_notch, Q, fs)
w_notch, h_notch = signal.freqz(b_notch, a_notch, worN=8000, fs=fs)

# 4. Combined System Response
h_total = h_band * h_notch

# 5. Plotting
plt.figure(figsize=(12, 6))
plt.semilogx(w_band, 20 * np.log10(abs(h_total)), label='Combined Filter Response', color='blue', linewidth=2)

# Highlighting the Notch
plt.axvline(f_notch, color='red', linestyle='--', alpha=0.7, label='50Hz Notch (Power-line)')

plt.title('Figure 2.1: Magnitude Response of the Multi-Layer Noise Mitigation Architecture', fontsize=12)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.ylim(-60, 5)
plt.xlim(0.1, 500)
plt.legend()

plt.show()