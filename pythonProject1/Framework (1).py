import cv2
import threading
from kivy.app import App
from kivy.uix.video import Video
import time
from kivy.config import Config
import subprocess
import numpy as np

Config.set('graphics', 'fullscreen', 'auto')


# set the filename for the recorded video
# output_file = 'cartoon_rec.mp4'


# create a function to record the screen and saves it to a video file
def record_screen():
    command = f"ffmpeg -f gdigrab -framerate 30 -offset_x 0 -offset_y 0 -video_size 1920x1080 -i desktop -c:v libx264 -preset ultrafast -pix_fmt yuv420p -ss 00:00:05 -to 00:00:25 -y cartoon_rec_1.mp4"

    # execute the command
    subprocess.Popen(command)


# create a function to record the audio and saves it to a audio file
def record_audio():
    command = f'ffmpeg -f dshow -i audio="Stereo Mix (Realtek(R) Audio)" -acodec pcm_s16le -ar 44100 -ac 2 -ss 00:00:05 -to 00:00:25 -y cartoon_audio_recording_12.wav'
    subprocess.run(command, shell=True)


# create a function to play the recorded video

def play_video(video_path, duration):
    # Launch ffmpeg subprocess to play the video
    ffmpeg_cmd = ['ffmpeg', '-i', video_path, '-vf', 'showinfo', '-autoexit']
    process = subprocess.Popen(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

    # Wait for the specified duration
    time.sleep(duration)

    # Terminate the ffmpeg process
    process.terminate()

# Example usage
video_path = 'cartoon_original.mp4'
duration = 34.6  # Duration in seconds
t1 = threading.Thread(target=record_audio)
t2 = threading.Thread(target=record_screen)
t1.start()
t2.start()
play_video(video_path, duration)

# creating a class for verifying the features of video
class Audio_Video_Testing:

    def __init__(self, original_video_path, recorded_video_path):

        self.original_video_path = original_video_path
        self.recorded_video_path = recorded_video_path

    # create a function to calculate the overall blur of a video
    def test_blurriness(self, video_path):

        # Open video file
        cap = cv2.VideoCapture(video_path)
        resolution = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        count = 0

        # Initialize variables
        prev_frame = None
        blurriness_scores = []

        # Loop through frames
        while True:
            # Read frame
            ret, frame = cap.read()
            count += 1

            # Check if we have reached the end of the video
            if not ret:
                break

            # Convert frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Compute blurriness score
            if prev_frame is not None:
                score = cv2.Laplacian(gray, cv2.CV_64F).var()
                blurriness_scores.append(score)
            prev_frame = gray

        # Compute average blurriness score
        avg_score = sum(blurriness_scores) / len(blurriness_scores)
        print(f"video:{video_path},resolution:{resolution} ")
        print("Avg_blurriness : ", avg_score)
        print("no of Frames :", len(blurriness_scores))
        # creating a text file to store the results
        fp = open("video_testing_results.txt", 'a')
        fp.write("the blurriness results\n")
        if avg_score < 50:
            print("The video is blurry.")
            fp.write(
                f"Blurriness verification video:{video_path},resolution:{resolution}\n Avg_blurriness : {avg_score}\n No of Frames : {len(blurriness_scores)}\n")
        elif avg_score > 50 and avg_score <= 100:
            print("The video is semi blur.")
            fp.write(
                f"video:{video_path},resolution:{resolution}\n Avg_blurriness : {avg_score}\n No of Frames : {len(blurriness_scores)}\n")

        else:
            print("the video is not blurr")
            fp.write(
                f"video:{video_path},resolution:{resolution}\n Avg_blurriness : {avg_score}\n No of Frames : {len(blurriness_scores)}\n")
        # close the file
        fp.close()

    # create a function to calculate the overall contrast of a video

    def cal_contrast(self, video_path):
        # Load the video file
        cap = cv2.VideoCapture(video_path)
        resolution = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

        max_value = []
        min_value = []
        # Loop through all frames in the video
        while True:
            # Read a frame from the video
            ret, frame = cap.read()

            # Check if the frame was successfully read
            if not ret:
                break

            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Compute the maximum and minimum luminance values in the frame
            #  max_frame = gray.max()
            #  min_frame = gray.min()
            max_value.append(gray.max())
            min_value.append(gray.min())

        lmax = sum(max_value) / len(max_value)
        lmin = sum(min_value) / len(min_value)

        # Calculate the contrast using the maximum and minimum luminance values
        contrast = (lmax - lmin) / (lmax + lmin)

        # Print the contrast value
        print(f"video : {video_path}  , resolution : {resolution}")
        print("Average max pixel value :", lmax)
        print("Average min pixel value :", lmin)
        print("Contrast: ", contrast)
        print("####################################################")
        # create a text file to store the result
        fp = open('video_testing_results.txt', 'a')
        fp.write("the contrast results\n")
        fp.write(
            f"video : {video_path}  , resolution : {resolution} \n Average max pixel value : {lmax} \n Average min pixel value : {lmin} \n Contrast: {contrast}\n ")
        # close the file
        fp.close()

    # create a function to calculate the freeze frames in a video
    def freeze_frames(self, video_path):
        cap = cv2.VideoCapture(video_path)
        resolution = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

        # Initialize variables
        prev_frame = None
        total_frame_count = 0
        freeze_frame_count = 0

        # Loop through the frames
        while cap.isOpened():
            # Read the next frame
            ret, frame = cap.read()

            # If the frame was not read successfully, exit the loop
            if not ret:
                break

            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # If this is the first frame, set it as the previous frame
            if prev_frame is None:
                prev_frame = gray
                continue

            # Calculate the absolute difference between the current and previous frames
            diff = cv2.absdiff(prev_frame, gray)
            total_frame_count += 1

            # Calculate the mean of the difference
            mean = cv2.mean(diff)[0]
            # print("mean value:{} ".format(mean))

            # If the mean is below a certain threshold, the frame is considered frozen
            if mean < 1:
                # Get the current frame number and timecode
                frame_number = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
                timecode = cap.get(cv2.CAP_PROP_POS_MSEC) // 1000
                # print("mean value:{} ".format(mean))
                freeze_frame_count += 1
                # Display the frame number and timecode
                # print("Freezing frame detected: Frame {}, Timecode {}".format(frame_number, timecode))

            # Set the current frame as the previous frame for the next iteration
            prev_frame = gray

        ratio = freeze_frame_count / total_frame_count

        print(f"video:{video_path},resolution:{resolution} \nFreeze ratio : ", ratio)
        print("Freeze Frame count : ", freeze_frame_count)
        print("Total Frame count : ", total_frame_count)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        # create a text file to store the results
        fp = open('video_testing_results.txt', 'a')
        fp.write("results for checking freeze of a video\n")
        fp.write(
            f"video : {video_path}  , resolution : {resolution} \n Freeze Frame Count :{freeze_frame_count}\n Total Frame count : {total_frame_count}\n")
        # close the file
        fp.close()
        # Release the video file
        cap.release()

    # create a function to slice the video
    def slice_verify(self, video_path):

        # Open the video file
        cap = cv2.VideoCapture(video_path)

        # Set the start and end times for counting frames
        start_time = 10  # Start time in seconds
        end_time = 30  # End time in seconds

        # Set the video frame rate
        fps = cap.get(cv2.CAP_PROP_FPS)

        # Set the frame count
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # Calculate the starting and ending frame numbers
        start_frame = int(start_time * fps)
        end_frame = int(end_time * fps)

        # Set the current frame number
        current_frame = start_frame

        # Iterate through the frames and count them
        frame_counter = 0
        while current_frame < end_frame:
            # Read the frame
            ret, frame = cap.read()

            # If the frame was successfully read
            if ret:
                # Increment the frame counter
                frame_counter += 1

                # Increment the current frame number
                current_frame += 1
            else:
                # If the frame couldn't be read, break out of the loop
                break
        # create a text file to store the results
        fp = open('video_testing_results.txt', 'a')
        fp.write("the slicing of a video\n")
        fp.write(
            f"Number of frames between {start_time} and {end_time} in original video: {frame_counter} \nFrames per second in original video: {fps}\n")
        # Open the video file
        cap = cv2.VideoCapture('sliced_video.mp4')
        # Set the video frame rate
        fps1 = cap.get(cv2.CAP_PROP_FPS)

        # Set the frame count
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # Print the results
        print(f"Number of frames in sliced video: {frame_count}")
        print(f"Frames per second in sliced video: {fps1}")

        fp.write(f"Number of frames in sliced video: {frame_count}\nFrames per second in sliced video: {fps1}\n")

    # create a function to find the frame positions of a video
    def frame_position(self, video_path):
        # Open the video file
        # filename = "rec_video5.mp4"
        cap = cv2.VideoCapture(video_path)

        # Get the video properties
        fps = cap.get(cv2.CAP_PROP_FPS)
        resolution = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        # fp = open("output_frame_pos.txt", 'w')
        # Loop through the frames and print the position, timecode, and frame properties
        fp = open('video_testing_results.txt', 'a')
        fp.write("verification of  frame position in a video\n")
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            position = cap.get(cv2.CAP_PROP_POS_FRAMES)
            timecode = cap.get(cv2.CAP_PROP_POS_MSEC)
            # print(timecode)
            timecode_line = f"{int(timecode // 3600000):02d}:{int(timecode // 60000 % 60):02d}:{int(timecode // 1000 % 60):02d}.{int(timecode % 1000):03d}"
            # print results
            print(
                f"video:{video_path},frame:{current_frame},Position: {int(position)}, Timecode: {timecode_line}, FPS: {fps}, Resolution: {resolution}\n")
            # open a file
            fp.write(
                f"video:{video_path},frame:{current_frame},Position: {int(position)}, Timecode: {timecode_line}, FPS: {fps}, Resolution: {resolution}\n")
        # Release the video file
        cap.release()

    # create a function to verify the resolution of a video
    def video_resolution(self):
        # Load original video
        original_video = cv2.VideoCapture(self.original_video_path)

        # Get original video resolution
        original_width = int(original_video.get(cv2.CAP_PROP_FRAME_WIDTH))
        original_height = int(original_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        original_resolution = (original_width, original_height)
        fp = open('video_testing_results.txt', 'a')
        fp.write("verification of video resolution\n")
        print(f"Original_Video_Resolution:{original_resolution}")
        fp.write(f"Original_Video_Resolution:{original_resolution}\n")

        # Load recorded video
        recorded_video = cv2.VideoCapture(self.recorded_video_path)

        # Get recorded video resolution
        recorded_width = int(recorded_video.get(cv2.CAP_PROP_FRAME_WIDTH))
        recorded_height = int(recorded_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        recorded_resolution = (recorded_width, recorded_height)
        print(f"Recorded_Video_Resolution:{recorded_resolution}")

        fp.write(f"Recorded_Video_Resolution:{recorded_resolution}\n")

        # Compare resolutions
        if original_resolution == recorded_resolution:
            print("Resolution match")
            fp.write(f"Resolution match\n")
        else:
            print("Resolution do not match")
            fp.write(f"Resolution do not match\n")
        cv2.destroyAllWindows()

    # create a function to calculate the overall brightness of a video
    def brightness_verification(self, video_path):
        # Load the original video
        cap = cv2.VideoCapture(video_path)

        # Initialize the brightness values list for original video
        brightness_vals = []

        # Loop through each frame in the original video
        while True:
            # Read the frame
            ret, frame = cap.read()

            # If there are no more frames, break the loop
            if not ret:
                break

            # Calculate the brightness of the frame
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            brightness = gray.mean()
            brightness_vals.append(brightness)

        # Calculate the overall brightness of the original video
        overall_brightness = sum(brightness_vals) / len(brightness_vals)
        # print results
        print(f"Overall brightness of {video_path}:{overall_brightness}\n")
        # open a file
        fp = open('video_testing_results.txt', 'a')
        fp.write("the brightness of a video results\n")
        fp.write(f"Overall brightness of {video_path}:{overall_brightness}\n")

        # Release the original video
        cap.release()

    # create a function to calculate the overall blackness of a video
    def black_test(self, video_path):
        fp = open('video_testing_results.txt', 'a')
        cap = cv2.VideoCapture(video_path)
        total_dark_pixels = 0
        total_pixels = 0
        num_frames = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            unwanted, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
            # print("unwanted value : ", unwanted)
            num_black_pixels = np.count_nonzero(binary == 0)
            total_dark_pixels += num_black_pixels
            total_pixels_per_frame = gray.shape[0] * gray.shape[1]
            total_pixels += total_pixels_per_frame
            num_frames += 1
        print(f"Total Dark pixel :{total_dark_pixels}\nTotal pixels :{total_pixels}\n")
        fp.write("the black level of a video\n")
        fp.write(f"Total Dark pixel :{total_dark_pixels}\nTotal pixels :{total_pixels}\n")
        # release the video
        cap.release()
        black_level = (total_dark_pixels / total_pixels) * 100

        fp.write(f"Black level :{black_level}\n")
        # print results
        print(f"Total Dark pixel :{total_dark_pixels}\nTotal pixels :{total_pixels}\nBlack level :{black_level}\n")

    # create a function to calculate the overall blockiness of a video
    def calculate_blockiness(self, video_path):
        # open a file
        fp = open('video_testing_results.txt', 'a')
        # Load the video file
        cap = cv2.VideoCapture(video_path)
        block_size = 8
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Get the bitrate of the video
        bitrate = int(cap.get(cv2.CAP_PROP_BITRATE))

        # Initialize variables
        total_blocks = 0
        total_variance = 0

        # Loop through each frame of the video
        while True:
            # Read the frame
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Divide the frame into blocks
            blocks = []
            for i in range(0, gray.shape[0], block_size):
                for j in range(0, gray.shape[1], block_size):
                    block = gray[i:i + block_size, j:j + block_size]
                    blocks.append(block)

            # Calculate the variance of each block
            for block in blocks:
                variance = np.var(block)
                total_variance += variance
                total_blocks += 1

        # Calculate the blockiness of the video
        blockiness = total_variance / total_blocks
        # print results
        print(f"video:{video_path}\nresolution:{frame_width}*{frame_height}\nBlockiness:{blockiness}")
        fp.write("the blockiness of a video\n")
        fp.write(f"video:{video_path}\nresolution:{frame_width}*{frame_height}\nBlockiness:{blockiness}")
        # Release the video capture object
        cap.release()

    # create a function to calculate the overall block loss of a video
    def block_loss(video_path):
        # open a file
        fp = open('video_testing_results.txt', 'a')
        # Load the video file
        cap = cv2.VideoCapture(video_path)

        # Initialize the variables
        total_frames = 0
        mse_sum = 0

        # Loop through all the frames in the video
        while True:
            # Read the frame
            ret, frame = cap.read()

            # Check if we have reached the end of the video
            if not ret:
                break

            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Apply a block-wise mean filter
            block_size = 4  # Set the block size (in pixels)
            mean = cv2.blur(gray, (block_size, block_size))

            # Calculate the mean squared error (MSE) between the original and filtered frames
            mse = np.mean((gray - mean) ** 2)

            # Add the MSE to the sum
            mse_sum += mse

            # Increment the total number of frames
            total_frames += 1
        print("filename", video_path)
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print("Resolution: {}x{}".format(frame_width, frame_height))

        # Get the bitrate of the video
        bitrate = int(cap.get(cv2.CAP_PROP_BITRATE))
        print("Bitrate: {} kbps".format(bitrate))

        # Release the video capture object
        cap.release()

        # Calculate the average MSE
        avg_mse = mse_sum / total_frames

        # Calculate the block loss as a percentage
        max_pixel_value = 255  # Set the maximum pixel value
        block_loss_percent = (avg_mse / max_pixel_value)
        # print results
        print(
            f"video:{video_path}\n resolution:{frame_width}*{frame_height}\nbitrate:{bitrate}\nblockloss:{block_loss_percent}\n")
        fp.write("the block loss of a video\n")
        fp.write(
            f"video:{video_path}\n resolution:{frame_width}*{frame_height}\nbitrate:{bitrate}\nblockloss:{block_loss_percent}\n")

    def Calling_fun(self):
        print("========Bluriness result of videos============")
        self.test_blurriness(self.original_video_path)
        self.test_blurriness(self.recorded_video_path)
        print("\n")
        print("=======Freezing result of a videos==========")
        self.freeze_frames(self.original_video_path)
        self.freeze_frames(self.recorded_video_path)
        print("\n")
        print("======= Contrast of a videos==========")
        self.cal_contrast(self.original_video_path)
        self.cal_contrast(self.recorded_video_path)
        print("\n")
        print("=======slicing results========")
        self.slice_verify(self.original_video_path)
        print("\n")
        print("========frame position verification==========")
        self.frame_position(self.original_video_path)
        self.frame_position(self.recorded_video_path)
        print("\n")
        print("========video Resolution verification==========")
        self.video_resolution()
        print("\n")
        print("========Brightness verification==========")
        self.brightness_verification(self.original_video_path)
        self.brightness_verification(self.recorded_video_path)
        print("\n")
        print("========Black level===========")
        self.black_test(self.original_video_path)
        self.black_test(self.recorded_video_path)
        print("=======Blockiness==========")
        self.calculate_blockiness(self.original_video_path)
        self.calculate_blockiness(self.recorded_video_path)
        print("\n")
        print("=======Block loss==============")
        self.block_loss(self.original_video_path)
        self.block_loss(self.recorded_video_path)


# creating a object
obj = Audio_Video_Testing("cartoon_original.mp4", "cartoon_rec_1.mp4")
obj.Calling_fun()
