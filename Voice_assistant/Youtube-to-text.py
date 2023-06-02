import pytube
video = 'https://www.youtube.com/watch?v=-LIIf7E-qFI'
data = pytube.YouTube(video)
# Converting and downloading as 'MP4' file
audio = data.streams.get_audio_only()
audio.download()