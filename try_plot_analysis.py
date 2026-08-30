from chord_bpm_detector.loader import load_audio
from chord_bpm_detector.analyze import analyze_audio
from chord_bpm_detector.viz import plot_analysis
import matplotlib.pyplot as plt

y,sr = load_audio("samples/chord_progression.wav")
result = analyze_audio("samples/chord_progression.wav")
plot_analysis(y,sr,result)
plt.show()