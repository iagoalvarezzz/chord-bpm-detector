from chord_bpm_detector.loader import load_audio

(y, sr) = load_audio("samples/test_tone.wav", sr=22050)
print(f"Type: {type(y)}, shape: {y.shape}, dtype: {y.dtype}, sr: {sr}, duration: {round(len(y)/sr,2)}")