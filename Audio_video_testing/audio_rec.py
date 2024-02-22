from kivy.app import App
import subprocess
import time
from kivy.clock import Clock
from kivy.uix.video import Video
from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')
import threading

def state_change(instance, state):
    if state == 'stop':
        App.get_running_app().stop()


def Audio():
    #output_file = 'ffmpeg_output_new1.mp4'
    #time.sleep(1)Stereo Mix (Realtek(R) Audio)
    # command = ['ffmpeg', '-f',  'dshow', '-i', 'audio=Stereo Mix (Realtek(R) Audio)',
    #            '-acodec', 'pcm_s16le', '-ar', '44100', '-ac', '2', '-t', '40.3', '-y','-ss','5','-to','35','org_aud_rec_1.wav']
    # # subprocess.Popen(command)
    command = f'ffmpeg -f dshow -i audio="Stereo Mix (Realtek(R) Audio)" -ss 00:00:05 -to 00:00:35 original_audio_rec.wav'
    subprocess.run(command, shell=True)
# def calculate_play_time():
#     # Open the video file
#     start_time = time.time()
#     video_file = open("original_video.mp4", "rb")
#     end_time = time.time()
#
#     # Calculate the time taken to open the video file
#     time_to_load = end_time - start_time
#     print("Time taken to load video:", time_to_load, "seconds")
#
#     # Start playing the video
#     start_time = time.time()
#     # your code to play the video goes here
#     end_time = time.time()
#
#     # Calculate the time taken to play the video
#     time_to_play = end_time - start_time
#     print("Time taken to play video:", time_to_play, "seconds")


def record_screen():
    # duration = 40.3
    # #delay = 2
    # output_file = 'new1_rec1.mp4'
    # resolution = '1920x1080'
    # fps = 30

    # command = ['ffmpeg', '-f', 'gdigrab', '-framerate', str(fps), '-offset_x', '0', '-offset_y', '0','-video_size',resolution,'-i', 'desktop', "-c:v", "libx264", "-preset", "ultrafast", "-pix_fmt", "yuv420p", '-t',str(duration), '-y','-ss','5','-to','35', output_file]
    #command = f'ffmpeg -f gdigrab -framerate 30 -offset_x 0 -offset_y 0 -video_size 1920x1080 -i desktop -c:v libx264 -preset ultrafast -pix_fmt yuv420p -ss 00:00:05 -to 00:00:35 -y cartoon_video_rec.mp4'
    command = f'ffmpeg -f gdigrab -framerate 30 -offset_x 0 -offset_y 0 -video_size 1920x1080 -i desktop -c:v libx264 -preset ultrafast -pix_fmt yuv420p -ss 00:00:05 -to 00:00:35 -y original_video_rec.mp4'
    subprocess.Popen(command)

def video_play():
    class VideoApp(App):
        def build(self):
            # create a video instance
            # video = Video(source='original_video.mp4', state='play', options={'allow_stretch': True})
            video = Video(source='original_video.mp4', options={'allow_stretch': True})
            # time.sleep(5)
            video.state = "play"
            # p = threading.Thread(target=new)
            # p.start()
            #p.start()
            p1 = threading.Thread(target=Audio)
            p2 = threading.Thread(target=record_screen)
            p1.start()
            p2.start()
            video.bind(state=state_change)
            # video.play=False
            return video
    VideoApp().run()

video_play()


# t1=threading.Thread(target=video_play)
# p1 = threading.Thread(target=Audio)
# p2 = threading.Thread(target=record_screen)
# t1.start()
# p1.start()
# p2.start()


