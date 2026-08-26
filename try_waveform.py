from chord_bpm_detector.loader import load_audio
from chord_bpm_detector.viz import plot_waveform

import matplotlib.pyplot as plt

(y, sr) = load_audio("samples/test_tone.wav")
y = y[:4*22050//440]
plot_waveform(y, sr)
plt.show()