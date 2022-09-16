import os
import requests
from bs4 import BeautifulSoup
import lxml
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint


# STEP 1: SPOTIFY AUTH AND URIs
SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")
SPOTIFY_USER_ID = os.environ.get("SPOTIFY_USER_ID")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
    )
)

user_id = sp.current_user()["id"]
# the above output "current_user" is a dictionary, must find the "id" key value
# print(sp.current_user())
# print(user_id)

# print(sp.current_user())
# print(sp.current_user_playing_track())

# STEP 2: GETTING ALL TITLES FROM A SPECIFIC DATE

date = input("Which year do you want to travel back in time to? Type the date in this format YYYY-MM-DD:")
#
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
response.raise_for_status()
# print(response.text)
billboard = response.text

soup = BeautifulSoup(billboard, "lxml")
songs = soup.find_all(name="h3", class_="a-no-trucate")
songs_list = [song.getText().strip("\n\t") for song in songs]
artists = soup.find_all("span", class_="a-no-trucate")
artists_list = [artist.getText().strip("\n\t") for artist in artists]
# print(songs_list)
# print(artists_list)

# final_list = dict(zip(artists_list, songs_list))
# print(final_list)


# STEP 3: CREATING A PLAYLIST

song_uris = []
year = date.split("-")[0]
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # pprint.pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist on Spotify. Skipped.")

# print(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)







