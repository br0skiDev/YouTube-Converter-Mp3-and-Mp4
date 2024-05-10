import requests
from dotenv import load_dotenv
import os
from moviepy.editor import VideoFileClip

load_dotenv()

url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"

print("\nPlease enter the YouTube video ID.\n\nHeres how to get the ID:\nYouTube link: .../watch?v=m81tcJpM7ng\nYouTube video ID: m81tcJpM7ng\n")
getVideoId = input("Enter ID: ")
querystring = {"videoId": getVideoId}

headers = {
    "X-RapidAPI-Key": os.getenv("X-RapidAPI-Key"),
    "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

if response.status_code == 200:
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Download Video
    video_url = data["videos"]["items"][0]["url"]
    video_title = data["title"]
    video_response = requests.get(video_url)
    if video_response.status_code == 200:
        video_filename = os.path.join(output_dir, f"{video_title}.mp4")
        with open(video_filename, "wb") as file:
            file.write(video_response.content)
        print("\nVideo downloaded and saved successfully.")

        # Convert to MP3
        mp3_filename = os.path.join(output_dir, f"{video_title}.mp3")
        video = VideoFileClip(video_filename)
        video.audio.write_audiofile(mp3_filename)
        video.close()

        print("\nMP3 created and saved successfully.")
    else:
        print("\nSomething went wrong while downloading the video.")
else:
    print("\nAPI didn't respond. Check the API key and internet connection.")
