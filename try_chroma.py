from chord_bpm_detector.loader import load_audio
from chord_bpm_detector.chords import compute_chroma
from chord_bpm_detector.viz import plot_chroma

import matplotlib.pyplot as plt

y,sr = load_audio("samples/chord_progression.wav")
chroma = compute_chroma(y,sr)
plot_chroma(chroma,sr)
plt.show()