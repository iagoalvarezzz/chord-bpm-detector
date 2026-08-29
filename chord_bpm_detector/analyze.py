from .loader import load_audio
from .tempo import estimate_tempo_and_beats
from .chords import (compute_chroma, build_chord_templates, 
  classify_chords, segment_chords, HOP)

def analyze_audio(path):
    audio, sr = load_audio(path)
    tempo, beat_times = estimate_tempo_and_beats(audio,sr)
    chroma = compute_chroma(audio,sr)
    templates = build_chord_templates()
    labels = classify_chords(chroma,templates)
    segments = segment_chords(labels,sr)
    total_data = {
      "duration_s": round(len(audio)/sr,2),
      "bpm": round(tempo,1),
      "n_beats": len(beat_times),
      "chords": [
        {"start": round(s,2), "end": round(e,2), "chord": c} for (s,e,c) in segments
      ]  
    }
    return total_data