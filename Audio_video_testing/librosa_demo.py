import librosa

# Load an audio file
audio_file = "cartoon_audio_recording.wav"
y, sr = librosa.load(audio_file)

# Compute MFCCs (Mel-frequency cepstral coefficients)
mfccs = librosa.feature.mfcc(y=y, sr=sr)

# Visualize the MFCCs
import librosa.display
import matplotlib.pyplot as plt

librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('MFCCs')
plt.show()
