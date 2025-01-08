import os
import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp
import json
# gets the users chosen directory and dumps it to a "temp" json
def get_dir() -> None :
    dir = filedialog.askdirectory()
    if dir :
        directory_var.set(dir)
        if os.path.isfile(path) :
            with open(os.path.join("C:\\", "vtemp", "dir.json"), "w") as json_f :
                json_f.write("")
            with open(os.path.join("C:\\", "vtemp", "dir.json"), "w") as json_f :
                json.dump({"dir" : dir}, json_f)
# gets url and pipes yt-dlp to download video over internet
def download_video() -> None :
    url = url_entry.get()
    directory = directory_var.get()
    if (not url) or (not directory) :
        messagebox.showerror("Error", "Please enter a video link and directory.") ; return
    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best',  # Download best video up to 1080p and best audio
        'merge_output_format': 'mp4',  # Merge video and audio into an MP4 file
        'outtmpl': os.path.join(directory, '%(title)s.%(ext)s'),  # Output filename template
    }
    
    # make a python script using yt_dlp to download a video from a specified link in 1080p quality
    
    try :
        with yt_dlp.YoutubeDL(ydl_opts) as ydl :
            ydl.download([url])
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as E :
        messagebox.showerror("Error", f"An error occurred: {str(E)}")
# root init
r = tk.Tk() ; r.title("Video Downloader") ; r.geometry("400x250") ; r.configure(bg = "#181818")
# dir storage and file presence check
directory_var = tk.StringVar()
path = os.path.join("C:\\", "vtemp", "dir.json")
if not os.path.exists(os.path.join("C:\\", "vtemp")) :
    os.makedirs(os.path.join("C:\\", "vtemp"))
if not os.path.isfile(path) :
    with open(path, "w") as json_f :
        json.dump({"dir" : directory_var.get()}, json_f)
else :
    with open(path, "r") as json_f :
        content = json.load(json_f)
    directory_var.set(content["dir"])
# objects
url_label = tk.Label(r, text = "Video URL:") ; url_label.pack(pady = 5) ; url_entry = tk.Entry(r, width = 50) ; url_entry.pack(pady = 5)
url_label.configure(fg = "#FFFFFF", bg = "#181818") ; url_entry.configure(fg = "#FFFFFF", bg = "#282828")
directory_button = tk.Button(r, text = "Select Directory", command = lambda : get_dir()) ; directory_button.pack(pady = 20)
directory_button.configure(fg = "#FFFFFF", bg = "#282828")
directory_label = tk.Label(r, textvariable = directory_var) ; directory_label.pack(pady = 5)
directory_label.configure(fg = "#FFFFFF", bg = "#181818")
download_button = tk.Button(r, text = "Download Video", command = lambda : download_video(), width = 42, height = 2) ; download_button.pack(pady = 20)
download_button.configure(fg = "#FFFFFF", bg = "#282828")
r.mainloop()