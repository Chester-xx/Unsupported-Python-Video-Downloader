# 1080p adaption into main app
# ->
# test ffmpeg installation
# ->
# add subprocess handler
# ->
# test subprocess method

# import subprocess
# subprocess.run(['ffmpeg', '-version'])

import os
import tkinter as tk
from tkinter import filedialog, messagebox
import json
import sys
import subprocess

# stdout/Terminal output of yt-dlp to tkinter label
class stdout :
    def __init__(self, label) :
        self.label = label
    def write(self, str_v) :
        self.label.config(text = str_v.rstrip("\n"))
    def flush(self) : pass

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
    url = url_entry.get() ; directory = directory_var.get() ; Err : str = "" ; c_url : bool = False ; c_dir : bool = False
    if (not url) : c_url = bool(True)
    if (not directory) : c_dir = bool(True)
    match (c_url, c_dir) :
        case (True, True) : Err = "Please enter a valid link and select a folder."
        case (False, False) : Err = ""
        case (True, False) : Err = "Please enter a valid link."
        case (False, True) : Err = "Please select a folder."   
    if Err != "" :
        messagebox.showerror("Error", Err) ; return
    
    ydl_opts = [
        'yt-dlp',
        '-f', 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        '--merge-output-format', 'mp4',
        '-o', os.path.join(directory, '%(title)s.%(ext)s'),
        url
    ]

    try:
        result = subprocess.run(ydl_opts, capture_output=True, text=True, check=True)
        messagebox.showinfo("Success", "Video downloaded successfully!")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred: {e.stderr.strip()}")
        

# root init
r = tk.Tk() ; r.title("Video Downloader") ; r.geometry("400x260") ; r.configure(bg = "#181818")
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
directory_button = tk.Button(r, text = "Select Folder", command = lambda : get_dir()) ; directory_button.pack(pady = 20)
directory_button.configure(fg = "#FFFFFF", bg = "#282828")
directory_label = tk.Label(r, textvariable = directory_var) ; directory_label.pack(pady = 5)
directory_label.configure(fg = "#FFFFFF", bg = "#181818")
download_button = tk.Button(r, text = "Download Video", command = lambda : download_video(), width = 42, height = 2) ; download_button.pack(pady = 20)
download_button.configure(fg = "#FFFFFF", bg = "#282828")
status_label = tk.Label(r, text = "") ; status_label.pack()
status_label.configure(fg = "#FFFFFF", bg = "#181818")
sys.stdout = stdout(status_label)
r.mainloop()


# test 1 -- No audio and file corrupted
# ydl_opts = [
#         'yt-dlp',
#         '-f', 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
#         '--merge-output-format', 'mp4',
#         '-o', os.path.join(directory, '%(title)s.%(ext)s'),
#         url
#     ]

#     try:
#         result = subprocess.run(ydl_opts, capture_output=True, text=True, check=True)
#         messagebox.showinfo("Success", "Video downloaded successfully!")
#         print(result.stdout)
#     except subprocess.CalledProcessError as e:
#         messagebox.showerror("Error", f"An error occurred: {e.stderr.strip()}")