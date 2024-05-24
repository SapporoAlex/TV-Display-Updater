import schedule
import time
import subprocess


# Function to play the video and stop at a scheduled time
def play_and_stop_video(video_path, stop_time):
    subprocess.Popen(["vlc", "--fullscreen", "--loop", video_path])
    schedule.every().day.at(stop_time).do(lambda: stop_video())


# Function to stop the video
def stop_video():
    subprocess.run(["taskkill", "/f", "/im", "vlc.exe"])


# Schedule tasks to play and stop videos at specific times
schedule.every().day.at('12:11').do(lambda: play_and_stop_video("vid1.avi", "12:12"))
schedule.every().day.at('12:12:05').do(lambda: play_and_stop_video("vid2.mp4", "12:13"))
schedule.every().day.at('12:13:05').do(lambda: play_and_stop_video("vid3.mp4", "12:14"))

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
