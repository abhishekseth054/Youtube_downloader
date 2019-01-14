from pytube import YouTube
import os
import requests
import re

def get_vedio_url(url):
    all_video_url = []
    try:
        res = requests.get(url)
    except:
        print('Please check your internet connection')
        return False

    response_text = res.text
    # print(res.text)

    if 'list=' in url:
        playlist_id_index = url.rfind('=') + 1
        # print(playlist_id_index) # 49
        playlist_id = url[playlist_id_index:]
        # print(playlist_id) # PLXmMXHVSvS-C_T5JWEDWIc9yEM3Hj52-1
    else:
        print('Something went wrong! Please check the Playlist url.')
        return False

    next_url_pattern = re.compile(r'watch\?v=\S+?list=' + playlist_id)
    # print(next_url_pattern)
    url_list = re.findall(next_url_pattern, response_text)
    # print(url_pattern_list)

    for new_url in url_list:
        new_url = new_url.replace('&amp;', '&')
        new_url = new_url.replace('\\u0026', '&')
        video_url = 'https://youtube.com/' + new_url
        # print(video_url)
        if video_url not in all_video_url:
            all_video_url.append(video_url)

    return all_video_url, playlist_id

playList_url = str(input("Enter Youtube Playlist url;"))
video_url_list, folder_name = get_vedio_url(playList_url)

if not os.path.isdir(folder_name):
    os.mkdir(folder_name)

save_path = os.path.join(os.getcwd(),folder_name)
# print(save_path)

available_video = []
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        path = os.path.join(root, name)
        if os.path.getsize(path) < 1:
            os.remove(path)
        else:
            available_video.append(str(name))

print('\nconnecting . . .\n')

for video_url in video_url_list:
    yt = YouTube(video_url)
    main_title = yt.title
    main_title = main_title + '.mp4'
    main_title = main_title.replace('|', '')
    if(main_title not in available_video):
        print(main_title + " download started")
        yt = yt.streams.filter(progressive=True, file_extension='mp4', res='720p').first()
        #yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        yt.download(save_path)
        print(main_title + " download completed")

print("download completed")

