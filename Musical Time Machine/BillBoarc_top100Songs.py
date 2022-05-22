# Musical Time Machine to get the top songs from a Particular Date in past.

from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to ?Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")

song_list = response.text
soup = BeautifulSoup(song_list, "html.parser")
the_list_songs = soup.select("li h3")
billboard_song_list = [the_list_songs[num].getText().strip() for num in range(0, 100)]
print(billboard_song_list)

with open("top100_songs.txt", mode='w') as file:
    for song in billboard_song_list:
        file.write(f"{song}\n")


"""import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="",
        client_secret="",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()[""]
"""