# Video Processing and Frame Extractor Using OpenCV and yt-dlp

## Overview:
This project allows users to capture multiple frames from a video file or a YouTube video by providing either a local video path or a YouTube URL. You can either download the video to your system or extract frames directly from an existing video file. Frames are captured at intervals and saved as image files in a specified folder. The code is well-commented for ease of understanding.

## Features:
- Download videos from YouTube using `yt-dlp`.
- Process local video files or YouTube videos to capture frames.
- Save frames at regular intervals as images.
- User-friendly prompts for path input and download options.
- Fully commented code for easy learning and adaptation.

## Technologies Used:
- **Python**: Core programming language.
- **OpenCV**: Used for reading videos and capturing frames.
- **yt-dlp**: Used for downloading YouTube videos.
- **OS Module**: Handles file paths and directories.

## How to Use:

### Requirements:
- Python 3.x
- Required Python libraries:
    - `opencv-python`
    - `yt-dlp`

### Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/YouTube-Frame-Extractor.git
   cd YouTube-Frame-Extractor
   ```
2. Install the required dependencies:
   ```bash
   pip install opencv-python yt-dlp
   ```

### Usage:
1. Run the script:
   ```bash
   python your_script_name.py
   ```

2. When prompted:
   - Enter the path of the local video file or YouTube URL.
   - Decide if you want to download the YouTube video or not.
   - Specify the path to save the downloaded video (if applicable).
   - Choose whether to capture frames from the video.
   - Specify the directory where the captured frames will be saved.

3. The program will automatically capture frames every 100 milliseconds from the video and save them as images in the specified directory.

4. Press 'q' to exit the frame capture process early if needed.

### Example:
```bash
Enter path/url to the video: https://www.youtube.com/watch?v=example_video
Do you want to download the YouTube video? (yes/no): yes
Enter the path where you want to download the video (e.g., C:\Users\YourUsername\Downloads): C:\Users\YourUsername\Downloads
Do you want to capture multiple frames of this video? (yes/no): yes
Enter the path where you want to save captured images (e.g., C:\Users\YourUsername\Images): C:\Users\YourUsername\Images
```

The program will download the video, process it, and save the frames as PNG images to your specified directory.

---

## Contributing:
Feel free to contribute by submitting pull requests or reporting issues!


