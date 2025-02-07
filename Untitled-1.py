import os
import urllib.request
import subprocess
import sys

def download_file(url, destination):
    """Download the file from the URL and save it to the destination path."""
    try:
        print(f"Downloading file from {url}...")
        urllib.request.urlretrieve(url, destination)
        print(f"Downloaded file to {destination}")
    except Exception as e:
        print(f"Error downloading file: {e}")
        sys.exit(1)

def run_executable(executable_path):
    """Run the downloaded executable."""
    try:
        print(f"Running the executable: {executable_path}")
        subprocess.run(executable_path, check=True)
        print("Executable ran successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running executable: {e}")
        sys.exit(1)

def main():
    url = "https://7-zip.org/a/7z2409-x64.exe"
    destination = "7z2409-x64.exe"
