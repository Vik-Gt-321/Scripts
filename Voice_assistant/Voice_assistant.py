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

def wiki_search(q = 'Putin'):
    results = wikipedia.search(q)
    page = wikipedia.page(results[1])
    content = page.content
    return content

# print(wiki_search())
spotify_search()
