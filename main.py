import spotipy
import os
import requests
import json

from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials and scope
SPOTIPY_CLIENT_ID = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'
SPOTIPY_REDIRECT_URI = 'http://localhost:8080'
SPOTIPY_SCOPE = 'playlist-modify-public'

# Initialize Spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=SPOTIPY_SCOPE))

# This function gets a list of tracks from a given URL or list of track names.
def get_track_list(input_data):
    """Gets a list of tracks from a given URL or list of track names."""
    if input_data.startswith('http'):
        # Input is a Spotify playlist URL
        playlist_id = input_data.split('/')[-1]
        playlist = sp.playlist_tracks(playlist_id)
        track_list = [track['track']['name'] for track in playlist['items']]
    else:
        # Input is a list of track names
        track_list = input_data.split('\n')
    return track_list

# This function downloads a list of tracks as MP3 files to a given output directory.
def download_track_list(track_list, output_dir):
    """Downloads a list of tracks as MP3 files to a given output directory."""
    os.makedirs(output_dir, exist_ok=True)
    for track in track_list:
        search_result = sp.search(q=track, type='track', limit=1)
        if search_result['tracks']['items']:
            track_id = search_result['tracks']['items'][0]['id']
            track_info = sp.track(track_id)
            track_name = track_info['name']
            artists = ', '.join([artist['name'] for artist in track_info['artists']])
            audio_features = sp.audio_features(track_id)[0]
            preview_url = track_info['preview_url']
            if preview_url:
                mp3_file = os.path.join(output_dir, f'{track_name} - {artists}.mp3')
                response = requests.get(preview_url)
                with open(mp3_file, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded: {track_name} - {artists}")
            else:
                print(f"No preview available for: {track_name} - {artists}")
        else:
            print(f"Track not found: {track}")

# Main function
if __name__ == '__main__':
    input_data = input("Enter a list of track names or a Spotify playlist URL:\n")
    output_dir = input("Enter the output directory for downloaded MP3 files:\n")

    track_list = get_track_list(input_data)
    download_track_list(track_list, output_dir)
