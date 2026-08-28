import librosa
import numpy as np

HOP = 512

def onset_envelope(y, sr):
  return librosa.onset.onset_strength(y=y, sr=sr, hop_length=HOP)

def estimate_tempo_and_beats(y, sr):
  (tempo, beat_frames) = librosa.beat.beat_track(y=y,sr=sr,hop_length=HOP)
  tempo = float(np.atleast_1d(tempo)[0])
  beat_times = librosa.frames_to_time(beat_frames, sr=sr, hop_length=HOP)
  return (tempo, beat_times)