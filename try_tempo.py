from chord_bpm_detector.loader import load_audio
from chord_bpm_detector.tempo import estimate_tempo_and_beats

y,sr = load_audio("samples/click_track.wav")
tempo,beat_times = estimate_tempo_and_beats(y,sr)
print("Tempo: ", tempo)
print("Number of beats: ", len(beat_times))
print("First beat times: ", beat_times[:4])