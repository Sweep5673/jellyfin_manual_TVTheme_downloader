import os
import yt_dlp

TV_SHOWS_DIR = r"Z:\media\tv"

def download_theme(show_path, show_name):
    theme_path = os.path.join(show_path, "theme.mp3")
    
    # Skip if theme already exists
    if os.path.exists(theme_path):
        print(f"Skipping {show_name} — theme already exists.")
        return

    query = f"{show_name} theme song"

    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': False,
        'outtmpl': os.path.join(show_path, "theme.%(ext)s"),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    print(f"\n Searching YouTube for: {query}")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([f"ytsearch1:{query}"])
            print(f"Downloaded theme for: {show_name}")
        except Exception as e:
            print(f"Failed to download theme for {show_name}: {e}")

def main():
    for show_name in os.listdir(TV_SHOWS_DIR):
        show_path = os.path.join(TV_SHOWS_DIR, show_name)
        # Only process directories, skip files
        if os.path.isdir(show_path):
            # Optional: skip season folders if they appear at this level
            if "Season" not in show_name:
                download_theme(show_path, show_name)

if __name__ == "__main__":
    main()
