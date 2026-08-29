import librosa
from scipy.ndimage import median_filter

HOP = 512

def compute_chroma(y,sr):
  chromagram = librosa.feature.chroma_cqt(y=y, sr=sr, hop_length=HOP)
  chromagram_smooth = median_filter(chromagram, size=(1,9))
  return chromagram_smooth