import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display

N_FFT = 2048
HOP = 512

def plot_waveform(y, sr, ax=None):
  if ax is None:
    _,ax = plt.subplots(figsize=(10,3))
  time = np.linspace (0,len(y)/sr,len(y), endpoint=False)  
  ax.plot(time, y)
  ax.set(xlabel="time", ylabel="amplitude", title="waveform")
  return ax

def plot_spectrum(y, sr, ax=None):
  if ax is None: 
    _,ax = plt.subplots(figsize=(10,3))
  n = min(len(y), sr)
  y_segment = y[:n]
  y_windowed = y_segment * np.hanning(n)
  y_fft = np.fft.rfft(y_windowed)
  y_magnitude = np.abs(y_fft)
  x = np.fft.rfftfreq(n, 1/sr)
  y_magnitude_dB = 20 * np.log10(y_magnitude + 1e-9)
  ax.semilogx(x,y_magnitude_dB)
  ax.set_xlim(20, sr/2)
  ax.set(xlabel="freq(Hz)", ylabel="magnitude(dB)", title="spectrum")

  peak_index = np.argmax(y_magnitude)
  print("Highest peak in: ", x[peak_index], "Hz")

  top5 = np.argsort(y_magnitude)[-5:]
  print("Top 5 frecuencies: ", x[top5])
  print("Top 5 magnitudes: ", y_magnitude[top5])
  
  return ax

def plot_spectrogram(y,sr,ax=None):
  if ax is None:
    _,ax = plt.subplots(figsize=(10,4))
  
  y_stft = librosa.stft(y, n_fft=N_FFT, hop_length=HOP)
  y_magnitude = np.abs(y_stft)
  y_magnitude_dB = librosa.amplitude_to_db(y_magnitude, ref=np.max)
  librosa.display.specshow(y_magnitude_dB, sr=sr, hop_length=HOP, 
    x_axis="time", y_axis="log", ax=ax)
  ax.set(title="spectrogram")
  return ax

def plot_chroma(chroma, sr, ax=None):
  if ax is None:
    _,ax = plt.subplots(figsize=(10,4))
  librosa.display.specshow(chroma,sr=sr,hop_length=HOP,
    x_axis="time",y_axis="chroma",ax=ax)
  ax.set(title="chromagram")
  return ax