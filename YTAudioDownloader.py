# from pytube import YouTube
# import os
#
# def download_youtube_audio_as_mp3(url, output_path='.'):
#     """
#     Downloads the audio of a YouTube video and saves it as an MP3 file.
#
#     Args:
#         url (str): The URL of the YouTube video.
#         output_path (str): The directory where the MP3 file will be saved.
#                            Defaults to the current directory.
#     """
#     try:
#         yt = YouTube(url)
#         # Filter for audio-only streams and get the first one (usually highest quality)
#         audio_stream = yt.streams.filter(only_audio=True).first()
#
#         if audio_stream:
#             print(f"Downloading audio for: {yt.title}...")
#             # Download the audio file
#             out_file = audio_stream.download(output_path=output_path)
#
#             # Rename the downloaded file to .mp3
#             base, ext = os.path.splitext(out_file)
#             new_file = base + '.mp3'
#             os.rename(out_file, new_file)
#
#             print(f"Successfully downloaded '{yt.title}' as MP3 to: {new_file}")
#         else:
#             print("No audio stream found for this video.")
#
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# if __name__ == "__main__":
#     video_url = input("Enter the YouTube video URL: ")
#     # You can specify a different output path if needed, e.g., 'C:/Users/YourUser/Music'
#     download_youtube_audio_as_mp3(video_url, 'C:/Users/jayes/Pictures/yt')


from pytube import YouTube

urls =  input("url:")

vid = YouTube(urls)

# video_download = vid.streams.get_highest_resolution()
audio_download = vid.streams.get_audio_only()

entry = YouTube(urls).title

print(f"\nVideo found: {entry}\n")

# print(f"Downloading Video...")
# video_download.download(filename=f"{entry}.mp4")

print("Downloading Audio...")
audio_download.download(filename=f"{entry}.mp3")

print("Program Completed")