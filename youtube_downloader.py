import yt_dlp
import os

def download_video(url, output_folder="downloads", format_choice='audio', bitrate=None):
    os.makedirs(output_folder, exist_ok=True)

    ydl_opts = {
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'noplaylist': True,
    }

    if format_choice == 'audio':
        if bitrate:
            ydl_opts['format'] = f'bestaudio[abr<={bitrate}]/bestaudio'
        else:
            ydl_opts['format'] = 'bestaudio'
    else:
        if bitrate:
            ydl_opts['format'] = f'bestvideo[height<={bitrate}]+bestaudio/best'
        else:
            ydl_opts['format'] = 'bestvideo+bestaudio/best'

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\nDownloading from: {url}")
            ydl.download([url])
        print("\nDownload complete! Files saved in 'downloads' folder.")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    print("=== YouTube Downloader ===")
    url = input("🔗 Enter YouTube URL: ").strip()

    if not url:
        print("No URL entered. Exiting...")
        exit()

    format_choice = ''
    while format_choice not in ['audio', 'video']:
        format_choice = input("Choose format ('audio' or 'video'): ").strip().lower()

    bitrate = None
    bitrate_input = input("Enter max bitrate (audio in kbps, video height in px) or leave blank for default: ").strip()
    if bitrate_input.isdigit():
        bitrate = int(bitrate_input)

    download_video(url, format_choice=format_choice, bitrate=bitrate)
