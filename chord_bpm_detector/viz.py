import matplotlib.pyplot as plt
import numpy as np

def plot_waveform(y, sr, ax=None):
  if ax is None:
    _,ax = plt.subplots(figsize=(10,3))
  time = np.linspace (0,len(y)/sr,len(y), endpoint=False)  
  ax.plot(time, y)
  ax.set(xlabel="time", ylabel="amplitude", title="waveform")
  return ax