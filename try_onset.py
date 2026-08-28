from chord_bpm_detector.loader import load_audio
from chord_bpm_detector.tempo import onset_envelope, HOP
import matplotlib.pyplot as plt
import librosa


audio, sr = load_audio("samples/click_track.wav")
y = onset_envelope(audio,sr=sr)
t = librosa.times_like(y, sr=sr, hop_length = HOP)
_,ax = plt.subplots(figsize=(10,3))
ax.plot(t, y)
ax.set(xlabel="time", ylabel="onset strength", title="onset strength envelope")
plt.show()