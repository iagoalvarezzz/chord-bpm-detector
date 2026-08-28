import librosa

HOP = 512

def onset_envelope(y, sr):
  return librosa.onset.onset_strength(y=y, sr=sr, hop_length=HOP)