# TODO
# ADD TO test-full-build, also integrate download of yt-dlp.exe to vtemp folder??

import os
import sys
import subprocess
import requests
from tkinter import messagebox
import tkinter as tk
import json

directory_var = tk.StringVar()

def start_test() -> None :
    # Checks presence of vtemp and dir,json, and sets initial folder location
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
    Get_ffmpeg()
    Update_Var()

def Get_ffmpeg() -> None :
    # download the 7z file
    messagebox.showwarning("Downloading Dependancy : FFMpeg", "Please wait a few moments")
    file_name = os.path.basename(r"ffmpeg-git-full.7z")
    res = requests.get("https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z")
    if (res.status_code == 200) :
        with open(file_name, "wb") as file :
            file.write(res.content)
    else : messagebox.showerror("Error", "Failed to download dependancy : FFMpeg.") ; quit()
    # unzip to Main drive
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(r"C:\ffmpeg", exist_ok = True)
    subprocess.run(["7z", "x", os.path.join(cur_dir, "ffmpeg-git-full.7z"), f"-oC:\\ffmpeg"], check = True, text = True)
    os.remove(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ffmpeg-git-full.7z"))

def Update_Var() -> None : 
    path1 = r"C:\Program Files\7-Zip"
    items = os.listdir(r"C:\\ffmpeg")
    # f"{[item for item in items if os.path.isdir(os.path.join(f"C:\\ffmpeg", item))][0]}"
    path2 = f"C:\\ffmpeg\\" + items[0] + r"\bin"
    print(path2)
    def Set(path) -> None :
        current_path = os.environ.get('PATH', '')

        if (path not in current_path) :
            new_path_variable = current_path + ';' + path
            os.environ['PATH'] = new_path_variable
            if (sys.platform == "win32") :
                import winreg as reg
                try:
                    reg_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment", 0, reg.KEY_SET_VALUE)
                    reg.SetValueEx(reg_key, "Path", 0, reg.REG_EXPAND_SZ, new_path_variable)
                    reg.CloseKey(reg_key)
                    print(f"Successfully added {path} to the PATH environment variable.")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to update PATH in the registry: {e}, please run program in administrator mode. If you have ran the application in administrator mode, you must restart your pc for changes to be made.")
        else:
            print(f"{path} is already in the PATH environment variable.")
    
    Set(path1)
    Set(path2)