from chord_bpm_detector.loader import load_audio
from chord_bpm_detector.chords import compute_chroma, build_chord_templates, classify_chords, segment_chords, HOP

y, sr = load_audio("samples/chord_progression.wav")
chroma = compute_chroma(y,sr=sr)
templates = build_chord_templates()
clas = classify_chords(chroma, templates)

n_clas = len(clas)
print(n_clas)
print(clas[int(1 * sr / HOP)])
print(clas[int(3 * sr / HOP)])
print(clas[int(5 * sr / HOP)])
print(clas[int(7 * sr / HOP)])

segmented_chords = segment_chords(clas, sr)
print(segmented_chords)