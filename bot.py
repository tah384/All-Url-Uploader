import requests
from bs4 import BeautifulSoup
import urllib

# Function to extract video URL from OTT website
def extract_video_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    video_tag = soup.find('video')
    if video_tag:
        video_url = video_tag['src']
        return video_url
    else:
        return None

# Function to download video from URL
def download_video(url, file_name):
    urllib.request.urlretrieve(url, file_name)

# Main function to handle Telegram bot requests
def handle_message(message):
    if message.startswith('/download'):
        url = message.split(' ')[1]
        video_url = extract_video_url(url)
        if video_url:
            download_video(video_url, 'downloaded_video.mp4')
            return 'Video downloaded successfully! 🎥📥'
        else:
            return 'Sorry, unable to extract video URL from the provided link. 😔'
    else:
        return 'Invalid command. Please use /download [OTT website URL] to download videos. 🚫'

# Sample usage
message = '/download https://www.example.com/video'
response = handle_message(message)
print(response)
