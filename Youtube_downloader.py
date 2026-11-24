from pytube import YouTube
import os

def download_video():
    print("=== YOUTUBE VIDEO DOWNLOADER ===")
    
    url = input("YouTube Video Link ivvu: ")
    
    try:
        yt = YouTube(url)
        print(f"\nTitle: {yt.title}")
        print(f"Channel: {yt.author}")
        print(f"Views: {yt.views}")
        
        print("\nDownloading...")
        # Highest quality lo download chesthundhi
        video = yt.streams.get_highest_resolution()
        video.download()
        
        print("Download Ayipoyindhi Varshi! ✅")
        print(f"File saved: {yt.title}.mp4")
        
    except Exception as e:
        print(f"Error vachindhi: {e}")
        print("Link correct o kadho okasari check cheyyi!")

if __name__ == "__main__":
    download_video()
