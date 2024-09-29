import cv2
import yt_dlp  # Using yt-dlp as an alternative to youtube_dl
import os

# Function to get the video stream URL from YouTube
def get_youtube_stream_url(url, download_decision, output_path):
    # ydl_opts dictionary contains options for the yt-dlp library, which is used to download videos from YouTube.
    ydl_opts = {
        'format': 'best',  # Get the best format
        'noplaylist': True,  # Only download a single video, not a playlist
        'quiet': False,  # Suppress output messages
        'outtmpl': os.path.join(output_path, '%(title)s.avi'),  # Output template
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=download_decision)  # Extract video information with downloading
        return os.path.join(output_path, f"{info['title']}.avi")  # Return the path of the downloaded video

# PROJECT: Capture multiple images from a video

# Get input from the user
path = input("Enter path/url to the video: ")

# Check if the input is a URL or a file path
if 'youtube.com' in path or 'youtu.be' in path:
    decisionDownload = input("[If you want to capture multiple images of your video, we recommend downloading the video to your system first and subsequently providing its local path on your machine. OR If you want to enjoy any video on your system, feel free to download in that case as well!] Do you want to download the YouTube video? (yes/no): ")
    
    # Determine the download decision based on user input
    decision = decisionDownload.lower() == "yes"
    
    if decision:
        download_path = input("Enter the path where you want to download the video (e.g., C:\\Users\\YourUsername\\Downloads): ")
        local_video_path = get_youtube_stream_url(path, decision, download_path)  # Fetch the YouTube stream URL and download
    else:
        local_video_path = path  # If not downloading, use the provided path directly
else:
    local_video_path = r"{}".format(path)  # Converts the path to a raw string

# Ask if they want to capture multiple images of the video
decision_capture = input("Do you want to capture multiple frames of this video? (yes/no): ")

if decision_capture.lower() == "yes":  # Used .lower() on user inputs to ensure that any case variation (like "Yes", "yes", "YES") is handled consistently.
    # Ask for the path where images will be saved
    output_image_path = input("Enter the path where you want to save captured images (e.g., C:\\Users\\YourUsername\\Images): ")

    # Use OpenCV to read the video stream
    vidcap = cv2.VideoCapture(local_video_path)  # Use the local video path
    
    # Check if the video opened successfully
    if not vidcap.isOpened():
        print("Error: Could not open video.")  # Error message if the video cannot be opened
    else:
        ret, image = vidcap.read()  # Read the first frame
        count = 0  # Initialize frame count
    
        while True:
            if ret:
                # Save the captured frame as a PNG file to the user-specified output path
                cv2.imwrite(os.path.join(output_image_path, f"img{count}.png"), image)  # Each image name will be unique.
                
                # Advance to the next frame every 100 milliseconds
                vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 100))
                
                # Read the next frame
                ret, image = vidcap.read()  # Read the next frame
                count += 1  # Increment the frame count
    
                # Press 'q' to exit
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break  # Exit loop if 'q' is pressed
            else:
                print("No more frames left. Images have been stored in your system.")  # End reached?
                break  # Exit the loop if no frame is returned
                
        # Release the video capture object
        vidcap.release()

# Clean up
cv2.destroyAllWindows()



#C:\Users\Shweta Tyagi\Computer Vision Project outputs