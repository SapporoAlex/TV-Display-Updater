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
schedule.every().day.at('08:00').do(lambda: play_and_stop_video("morning.avi", "11:00"))
schedule.every().day.at('11:00:01').do(lambda: play_and_stop_video("lunch.mp4", "14:30"))
schedule.every().day.at('14:30:01').do(lambda: play_and_stop_video("afternoon.mp4", "18:00"))

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
