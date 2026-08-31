import numpy as np
from chord_bpm_detector.chords import build_chord_templates, classify_chords

def test_c_major_template_detects_c_major():
  templates = build_chord_templates()
  chroma = np.zeros((12,1))
  chroma[[0,4,7],0] = 1
  labels = classify_chords(chroma,templates)
  assert labels[0] == "C:maj"