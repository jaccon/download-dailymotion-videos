import youtube_dl

def download_hook(d):
    if d['status'] == 'downloading':
        percent_str = d.get('_percent_str', '0%').strip().replace('%', '')
        print(f"Download progress: {percent_str}")

def download_dailymotion_videos_from_playlist(playlist_file, save_path):
    with open(playlist_file, 'r') as file:
        video_urls = file.readlines()
    
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'progress_hooks': [download_hook],
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for video_url in video_urls:
            ydl.download([video_url.strip()])
            print(f"Video from {video_url.strip()} downloaded successfully!")

# Example usage
playlist_file = "playlist.txt"
save_path = "downloads"
download_dailymotion_videos_from_playlist(playlist_file, save_path)
