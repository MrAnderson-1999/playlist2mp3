# This script gets a list of tracks from a given URL and
# either downloads the tracks to a given output directory or adds
# the tracks to a given playlist.

import spotipy
import requests
import json

# This function gets a list of tracks from a given URL.
def get_track_list(url):
  """Gets a list of tracks from a given URL."""
  # Make a request to the URL.
  response = requests.get(url)

  # Check if the request was successful.
  if response.status_code == 200:
    # The request was successful, so load the JSON data.
    data = json.loads(response.content)

    # Create a list of tracks.
    track_list = []

    # Iterate over the tracks in the JSON data.
    for track in data['tracks']['items']:
      # Add the track name to the list of tracks.
      track_list.append(track['track']['name'])

    # Return the list of tracks.
    return track_list

  else:
    # The request failed, so raise an exception.
    raise Exception("Failed to get track list: {}".format(response.status_code))

# This function downloads a list of tracks to a given output directory.
def download_track_list(track_list, output_dir):
  """Downloads a list of tracks to a given output directory."""
  # Iterate over the tracks in the list.
  for track in track_list:
    # Get the track URI.
    request = spotipy.client.TrackRequest(track)
    uri = request.get()['uri']

    # Download the track to the output directory.
    spotipy.client.DownloadFile(uri, os.path.join(output_dir, track))

# This function adds a list of tracks to a given playlist.
def add_track_list_to_playlist(track_list, playlist_id):
  """Adds a list of tracks to a given playlist."""
  # Create a Spotify client.
  client = spotipy.client.Spotify()

  # Add the tracks to the playlist.
  client.user_playlist_add_tracks(playlist_id, track_list)

# This is the main function.
if __name__ == '__main__':
  # Get the track list from the user.
  url = input("Enter the URL of the track list: ")
  track_list = get_track_list(url)

  # Choose whether to download the tracks or add them to a playlist.
  action = input("Would you like to download (d) or add to playlist (a): ")
  if action == 'd':
    # Get the output directory from the user.
    output_dir = input("Enter the output directory: ")
    download_track_list(track_list, output_dir)
  elif action == 'a':
    # Get the playlist ID from the user.
    playlist_id = input("Enter the playlist ID: ")
    add_track_list_to_playlist(track_list, playlist_id)
  else:
    print("Invalid action.")
