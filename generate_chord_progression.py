import numpy as np
import soundfile as sf

def generate_chord(f1,f2,f3,chord_duration=2,sr=22050):
  t = np.linspace(0,chord_duration,sr*chord_duration,endpoint=False)
  tone_1 = np.sin(2 * np.pi * f1 * t)
  tone_2 = np.sin(2 * np.pi * f2 * t)
  tone_3 = np.sin(2 * np.pi * f3 * t)
  return tone_1 + tone_2 + tone_3

sr = 22050
#Variables to save different frequencies of notes:
a4 = 440
c4 = a4 * 2**(-9/12)
e4 = a4 * 2**(-5/12)
g4 = a4 * 2**(-2/12)
b4 = a4 * 2**(2/12)
d5 = a4 * 2**(5/12)
f4 = a4 * 2**(-4/12)
c5 = a4 * 2**(3/12)


cMaj = generate_chord(c4,e4,g4)
fMaj = generate_chord(f4,a4,c5)
gMaj = generate_chord(g4,b4,d5)

chord_progression = np.concatenate([cMaj,fMaj,gMaj,cMaj])
sf.write("samples/chord_progression.wav", chord_progression, sr)
print("Generated: samples/chord_progression.wav")


