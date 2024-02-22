import pyaudio
import wave

def verify_audio_properties(file_path):
    p = pyaudio.PyAudio()

    # Open the audio file
    wf = wave.open(file_path, 'rb')

    print(f"File: {file_path}")
    print(f"Sample Width: {wf.getsampwidth()} bytes")
    print(f"Sample Rate: {wf.getframerate()} Hz")
    print(f"Channels: {wf.getnchannels()}")
    print(f"Frames: {wf.getnframes()}")
    print(f"Duration: {wf.getnframes() / wf.getframerate()} seconds")

    wf.close()
    p.terminate()

if __name__ == "__main__":
    audio_file_path = "cartoon_audio_recording.wav"  # Replace with your audio file path
    verify_audio_properties(audio_file_path)
