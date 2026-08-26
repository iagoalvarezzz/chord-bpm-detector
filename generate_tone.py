import numpy as np
import soundfile as sf

sr = 22050          # sample rate
duration = 3        # seconds
t = np.linspace(0, duration, int(sr * duration), endpoint=False)
tone = 0.5 * np.sin(2 * np.pi * 440 * t)  # A4 (440 Hz), 3 seconds
sf.write("samples/test_tone.wav", tone, sr)
print("Generated: samples/test_tone.wav")
