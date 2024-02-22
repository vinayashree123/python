import librosa
import matplotlib.pyplot as plt


def audio_glitch(audio_file):
    # Load audio file
    # audio_file = 'path/to/audio_file.wav'
    y, sr = librosa.load(audio_file)

    librosa.display.waveshow(y)
    plt.show()
    # Calculate onset envelope
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)

    # Detect onset events
    onsets = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
    # Calculate the inter-onset intervals (IOIs)
    iois = librosa.frames_to_time(onsets[1:] - onsets[:-1], sr=sr)
    # Calculate the average IOI
    avg_ioi = iois.mean()

    # Calculate the audio glitch as a percentage of the average IOI
    glitch_pct = len(iois[iois > avg_ioi]) / len(iois) * 100

    # Print the audio glitch percentage
    print(f"Audio Glitch: {glitch_pct:.2f}%")
    print("No of iois is Greater than Avg : ", len(iois[iois > avg_ioi]))
    print("Total No of ioi's  : ", len(iois))
    print("Average iois : ", avg_ioi)


print("Original Audio")
audio_glitch("cartoon_audio_recording.wav")
print("\n")
print("Record Audio")
audio_glitch("original_audio_recording.wav")

# print("Original Audio")
# Audio_Glitch("sample.wav")
# print("\n")
# print("Recorded Audio")
# Audio_Glitch("new_aud_rec.wav")
# print("\n")
# print("Glitch Sample  Audio")
# Audio_Glitch("glitch_audio.wav")
# print("\n")

# Audio_Glitch("sample.wav")


#
# import pydub
#
# def Glitch(Audio_path):
#     audio=pydub.AudioSegment.from_file(Audio_path,format='wav')
#     silence_intervals=pydub.silence.detect_silence(audio,min_silence_len=100,silence_thresh=-50)
#     for i in range(1,len(silence_intervals)):
#         if silence_intervals[i][0]-silence_intervals[i-1][1]<50:
#             print(f"glitch detected between {silence_intervals[i-1][1]/1000:.3f}s and {silence_intervals[i][0]/1000:.3f}s")
#
#
# print("Original Audio ")
# Glitch("new_aud_org.wav")
# print("Recorded Audio")
# Glitch("new_aud_rec.wav")
#



#
# import matplotlib.pyplot as plt
# import numpy as np
# import wave
#
# # Read in the first audio file
# file1 = "sample.wav"
# with wave.open(file1, 'r') as wave_file:
#     data1 = np.frombuffer(wave_file.readframes(-1), dtype='int16')
#     framerate1 = wave_file.getframerate()
#
# # Read in the second audio file
# file2 = "sample_Record.wav"
# with wave.open(file2, 'r') as wave_file:
#     data2 = np.frombuffer(wave_file.readframes(-1), dtype='int16')
#     framerate2 = wave_file.getframerate()
#
# # Create a time axis for the plots
# time1 = np.arange(0, len(data1)) / framerate1
# time2 = np.arange(0, len(data2)) / framerate2
#
# # Plot the first audio file in blue
# plt.plot(time1, data1, color='blue', linestyle='solid', label='File 1')
#
# # Plot the second audio file in red
# plt.plot(time2, data2, color='red', linestyle='dashed', label='File 2')
#
# # Add a legend and axis labels
# plt.legend()
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
#
# # Show the plot
# plt.show()
