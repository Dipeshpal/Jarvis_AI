from pytube import YouTube
import os


def download_yt_video(inp_command):
    ytURL = input("Enter the URL of the YouTube video: ")
    yt = YouTube(ytURL)
    try:
        print("Downloading...")
        yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution")[-1].download()
    except:
        return "ERROR | Please try again later"
    return f"Download Complete | Saved at {os.getcwd()}"


if __name__ == "__main__":
    download_yt_video()
