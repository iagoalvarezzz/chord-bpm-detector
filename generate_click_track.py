import numpy as np
import soundfile as sf

bpm = 120
duration = 8
sr = 22050

interval = 60 / bpm
beat_times = np.arange(0, duration, interval)
signal = np.zeros(int(sr * duration))
for time in beat_times:
  index = int(time * sr)
  signal[index] = 1
sf.write("samples/click_track.wav", signal, sr)
print("Generated: samples/click_track.wav")


