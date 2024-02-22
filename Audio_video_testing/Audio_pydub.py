from pydub import AudioSegment

# Define the path to the audio file
audio_file = "your_audio_file.mp3"

# Load the audio file using PyDub
audio = AudioSegment.from_file(audio_file)

# Get audio properties
duration_seconds = len(audio) / 1000.0  # Duration in seconds
channels = audio.channels
sample_width = audio.sample_width
frame_rate = audio.frame_rate
frame_width = audio.frame_width

# Print the audio properties
print(f"Duration: {duration_seconds} seconds")
print(f"Channels: {channels}")
print(f"Sample Width: {sample_width} bytes")
print(f"Frame Rate: {frame_rate} Hz")
print(f"Frame Width: {frame_width} bytes")
