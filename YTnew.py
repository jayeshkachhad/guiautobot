# import yt_dlp
#
# def download_audio_yt_dlp(url, output_path='.'):
#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'outtmpl': f'{output_path}/%(title)s.%(ext)s',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#     }
#
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
#
# if __name__ == "__main__":
#     video_url = input("Enter YouTube video URL: ")
#     download_audio_yt_dlp(video_url, 'D:\YT')


import yt_dlp

def download_audio_only(url, output_path='.'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Saves with original extension (like .webm or .m4a)
        # No postprocessors
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":

    video_urls = [
        "https://youtu.be/Z009mu-guyA?si=4YrOK10YjjWTV_jS",
        "https://youtu.be/rg0_lCXItdI?si=Ihvh9SaDxgQnJFS_",
        "https://youtu.be/iBWQuEpmAPE?si=stRCGHFpJv9iGErJ",
        "https://youtu.be/4sMhBtMej8U?si=p5z5KxxWL-GIcRFY",
        "https://youtu.be/axdxg_JIaKQ?si=Lbj0RsL9FRYIqcCw",
        "https://youtu.be/OX9mZ51oj5M?si=OkvCQFly3agkMCgF",
        "https://youtu.be/_nIvLtBDIlQ?si=A5mzoceNk-tZ5oUB",
        "https://youtu.be/6wsNqbzzXJ4?si=0934-PVWAU4_aZF_",
        "https://youtu.be/SydwTg4SZbI?si=60m_hQKrNgSN6TPw",
        "https://youtu.be/VdHIzKM9UnQ?si=uXji4E_BZXXnrmpI",
        "https://youtu.be/c4ef1V9Kdx0?si=p3Og1rIdlnwKISN1",
        "https://youtu.be/SyjQa1gfyyA?si=G-_IeBLzhOQF_Kln",
        "https://youtu.be/Y8Njv2AG3Pw?si=IghbzDORHiWp6Fnz",
        "https://youtu.be/btxl3i6ujXA?si=MaK6lVRmfKZ03cej",
        "https://youtu.be/neMF8QEzVyk?si=MbbSrvGBLavEVyuL",
        "https://youtu.be/QLbKbNvcYto?si=hSJMAE-RM04A8Szm",
        "https://youtu.be/F-h1QRPrvYU?si=xpUnE-ojEEmSZIGP",
        "https://youtu.be/ki6T8D-TXac?si=j1Bs1OQSIBL_Ee5B",
        "https://youtu.be/I8-tPlkxjcA?si=OvS7zTSrMXIeIXv2",
        "https://youtu.be/3GlibsMMn2o?si=Jsu39Es3vq5-VcZn",
        "https://youtu.be/SJ0FwA9ug6A?si=219jsCGCGvf4yOg5",
        "https://youtu.be/3CBxODJlNjY?si=udGY93KkqZv8SSvf",
        "https://youtu.be/f_9JUPRW2WA?si=BAtbNXkumzE5u6zd",
        "https://youtu.be/1mytL1KEf9A?si=d2UmsETxhBBFMhH6",
        "https://youtu.be/1qbgqGw0Brk?si=0G3L__KCTmFDj8nT",
        "https://youtu.be/TsLfzHa4bTo?si=HpzY849iNDkXYzxF",
    ]

    for url in video_urls:
        print(f"Downloading: {url}")
        download_audio_only(url, r'D:\YT')  # Make sure this folder exists