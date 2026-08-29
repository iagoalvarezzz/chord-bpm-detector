from chord_bpm_detector.analyze import analyze_audio

data = analyze_audio("samples/chord_progression.wav")
for key, value in data.items():
  print(key, value)