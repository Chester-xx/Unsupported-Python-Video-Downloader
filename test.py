# 1080p adaption into main app

import yt_dlp

import subprocess
subprocess.run(['ffmpeg', '-version'])

def download_video(url):
    ydl_opts = {
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
    'outtmpl': '%(title)s.mp4',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }],
}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the video URL: ")
    download_video(video_url)
    print("Download completed!")