from os import environ
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# Web Scraping
date = input("Which year you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(url="https://www.billboard.com/charts/hot-100/" + date)
site = response.text

soup = BeautifulSoup(site, "html.parser")
top100Songs = [title.getText().strip() for title in soup.select(selector="h3#title-of-a-story")]


# Spotify authentication
user_name = input("Enter your spotify user name: ")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=environ.get('spotifyclientid'),
        client_secret=environ.get('spotifyclientsecret'),
        show_dialog=True,
        cache_path="token.txt",
        username=f"{user_name}", 
    )
)
user_id = sp.current_user()["id"]


# Searching spotify for songs by title
song_uris = []
year = date.split('-')[0]
for song in top100Songs:
    result = sp.search(q=f"track:{song} year={year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Top 100", public=False)
print(playlist)


#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
