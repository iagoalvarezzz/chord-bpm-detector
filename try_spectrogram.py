from chord_bpm_detector.loader import load_audio
from chord_bpm_detector.viz import plot_spectrogram

import matplotlib.pyplot as plt

(y,sr) = load_audio("samples/test_tone.wav")
plot_spectrogram(y,sr)
plt.show()