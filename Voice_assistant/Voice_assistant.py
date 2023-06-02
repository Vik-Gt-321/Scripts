import wikipedia
import wolframalpha
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def spotify_search(q='track:Believer artist:Imagine Dragons'):
    client_id = '3cdfdc87160c4e09bb14a8aa23d94e87'
    client_secret = '66d0664b94b0465393b2db1c81ecba8c'

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # results = sp.search(q = q, type='track')
    # for track in results['tracks']['items']:
    #     # print(track['name'], 'by', track['artists'][0]['name'])

    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])
    # track_uri = results['tracks']['items'][0]['uri']

    # # Play the preview of the track
    # sp.start_playback(uris=[track_uri])

def wolf_search(q = "What is the weather like today?"):
    app_id = '5LTGY4-AV5V2UEKXV'
    client = wolframalpha.Client(app_id)
    res = client.query(q)
    answer = next(res.results).text
    return answer

def wiki_search():
    q = "Vladimir Putin"
    results = wikipedia.search(q)
    page = wikipedia.page(results[1])
    content = page.content
    print(page.url, page.title)
    # wikipedia.set_lang("fr")

# print(wiki_search())
# print(wolf_search())

# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyaudio

p = pyaudio.PyAudio()

# Get the default input device index
default_device_index = p.get_default_input_device_info()['index']

# Get the default input device info
default_device_info = p.get_device_info_by_index(default_device_index)

# Print the default input device info
print("Default Input Device:")
print("Name: ", default_device_info['name'])
print("Channels: ", default_device_info['maxInputChannels'])
print("Sample Rate: ", default_device_info['defaultSampleRate'])

# Terminate PyAudio
p.terminate()

r = sr.Recognizer()
print(pyaudio.get_default_input_device_info())
with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)



