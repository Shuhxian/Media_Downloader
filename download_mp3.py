from pytube import YouTube
import os
from moviepy.editor import *
import sys
if len(sys.argv)<2:
    print("Video link expected!")
    raise SystemExit(2)
video_link=sys.argv[1]
output=sys.argv[2] if len(sys.argv)==3 else 'test.mp3'
yt = YouTube(video_link)
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first().download(filename='test.mp4')
video = VideoFileClip(os.getcwd()+'/test.mp4')
video.audio.write_audiofile(os.getcwd()+"/"+output)
os.remove("test.mp4")