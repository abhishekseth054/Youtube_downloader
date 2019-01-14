from pytube import YouTube
import os

def downloadYouTube(videourl, path):
    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

video_url = "https://www.youtube.com/watch?v=MtQL_ll5KhQ"
folder_name = "YoutubeVideo"
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)

save_path = os.path.join(os.getcwd(),folder_name)

	
downloadYouTube(video_url, save_path)