# Video Scheduler
This script automates the scheduling of video playback using VLC media player. It plays specific videos at designated times and stops them at specified end times. The script uses the `schedule` library to manage timing and `subprocess` to handle VLC media player processes.
This was designed for a resturant in Sapporo, Hokkaido who wanted to have their display screens show different specials at different times
throughout the day without having to manually change their pre-made videos.

## Prerequisites

Ensure you have the following installed on your system:
- Python 3.x
- VLC media player
- Python libraries: `schedule`, `time`, `subprocess`

You can install the required Python libraries using pip:
```sh
pip install schedule
```
## Script Description
### Functions
- play_and_stop_video(video_path, stop_time)
  -Plays the video located at video_path in fullscreen mode and schedules it to stop at stop_time.
   - Arguments:
- video_path: Path to the video file to be played.
  - stop_time: Time (in HH:MM format) when the video should stop.
  - stop_video()
    -Stops the VLC media player by terminating its process.

### Scheduling Tasks
The script schedules the playback of three videos at different times of the day:

- Morning Video
  - Starts at 08:00 and stops at 11:00.
  - Plays morning.avi.
- Lunch Video
  - Starts at 11:00:01 and stops at 14:30.
  - Plays lunch.mp4.
- Afternoon Video
  - Starts at 14:30:01 and stops at 18:00.
  - Plays afternoon.mp4.
### Continuous Running
The script runs indefinitely, checking and executing scheduled tasks every second.

## Usage
1. Prepare the Video Files:
- Ensure morning.avi, lunch.mp4, and afternoon.mp4 are available in the specified paths.

2. Run the Script:
- Execute the script using Python:
```sh
python video_scheduler.py
```
- Ensure VLC media player is installed and accessible from the command line.

## Example Code
```bash
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
```

## Notes
- Ensure the script has the necessary permissions to execute the taskkill command on your system.
- Modify the video paths and scheduled times as needed to fit your requirements.
- For Linux or macOS systems, replace the taskkill command with the appropriate command to terminate VLC (e.g., pkill vlc).

## Troubleshooting
- If the videos do not play or stop as expected, verify the paths to the video files and the availability of VLC media player.
- Ensure the system's time settings are correct and synchronized.
This script provides a basic framework for scheduling video playback using VLC. Customize it further to suit your specific needs and environment.
