import librosa

def load_audio(path, sr = 22050):
  """Load an audio file as a mono signal.
  Returns (y, sr): y is a float32 np.ndarray in [-1,1],
  sr is the resulting sample rate.
  
  """
  return librosa.load(path, sr=sr, mono=True)
