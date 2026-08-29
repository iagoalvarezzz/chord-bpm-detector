import librosa
import numpy as np
from scipy.ndimage import median_filter

HOP = 512
PITCHES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def compute_chroma(y,sr):
  chromagram = librosa.feature.chroma_cqt(y=y, sr=sr, hop_length=HOP)
  chromagram_smooth = median_filter(chromagram, size=(1,9))
  return chromagram_smooth

def build_chord_templates():
  templates = {}
  for i, root in enumerate(PITCHES):
    maj_template = np.zeros(12)
    maj_template[[i,(i+4)%12,(i+7)%12]] = 1
    min_template = np.zeros(12)
    min_template[[i,(i+3)%12,(i+7)%12]] = 1
    templates[f"{root}:maj"] = maj_template
    templates[f"{root}:min"] = min_template
  return templates
  
def classify_chords(chroma, templates):
  names = list(templates.keys())
  T = np.stack([templates[n] for n in names])
  T = T / np.linalg.norm(T, axis=1, keepdims=True)
  C = chroma / (np.linalg.norm(chroma, axis=0, keepdims=True) + 1e-9)
  sim = T @ C
  idx = sim.argmax(axis=0)
  return [names[i] for i in idx]