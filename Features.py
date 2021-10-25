# import modules and packages
import librosa as lr
import librosa.display
import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np
# set directory for audio files
audio_file="Desktop/Project/snd/horn.wav"
ipd.Audio(audio_file)
signal.shape
#Extract MFCCs
mfccs=librosa.feature.mfcc(signal,n_mfcc=13,sr=sr)
mfccs.shape
#visualize MFCCs
plt.figure(figsize=(25,10))
librosa.display.specshow(mfccs,x_axis="time",sr=sr)
plt.colorbar(format="%+2f")
plt.show()
#visualize MFCCs
plt.figure(figsize=(25,10))
librosa.display.specshow(mfccs,x_axis="time",sr=sr)
plt.colorbar(format="%+2f")
plt.show()
mfccs.shape
delta_mfccs.shape
delta2_mfccs.shape
#visualize deltaMFCCs
plt.figure(figsize=(25,10))
librosa.display.specshow(delta_mfccs,x_axis="time",sr=sr)
plt.colorbar(format="%+2f")
plt.show()
#visualize delta2MFCCs
plt.figure(figsize=(25,10))
librosa.display.specshow(delta2_mfccs,x_axis="time",sr=sr)
plt.colorbar(format="%+2f")
plt.show()
comprehensive_mfccs=np.concatenate((mfccs,delta_mfccs,delta2_mfccs))
comprehensive_mfccs.shape
output = np.mean(comprehensive_mfccs)
