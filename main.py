import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

#account authentication
scope = 'playlist-modify-public'
username = '316gtg77lgfwkteacpw4zelpjbla'

token = SpotifyOAuth(scope=scope,username=username)
spotifyObject = spotipy.Spotify(auth_manager = token)

#input playlist name and description
playlist_name = input("Enter a playlist name :")
playlist_description = input("Enter a playlist description : ")

#input songs
user_input = input("Enter the song : ")
list_of_songs = []

while user_input != 'quit':
        result = spotifyObject.search(q = user_input)
        list_of_songs.append(result['tracks']['items'][0]['uri'])
        user_input = input("Enter the song : ")

#accessing and creating the playlist
spotifyObject.user_playlist_create(user=username,name=playlist_name,public=True,description=playlist_description)
prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

#adding tracks
spotifyObject.user_playlist_add_tracks(user=username,playlist_id=playlist,tracks=list_of_songs)
