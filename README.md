# playlist2mp3
Any list of names of track will be downloaded as mp3 or added to Spotify

## Track List Manager

This script allows you to work with a list of tracks from a given URL. You can either download the tracks to a specified output directory or add them to a playlist.

## Features

- Fetch a list of tracks from a given URL.
- Download tracks to a designated output directory.
- Add tracks to a specified Spotify playlist.

## Prerequisites

- Python 3.x
- Spotipy: A lightweight Python library for the Spotify Web API.
- Requests: A Python library for making HTTP requests.
- An active Spotify account.

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

- Run the script using the following command:
`python main.py`
Follow the prompts to interact with the script.

## Functions
- `get_track_list(url)`: Gets a list of tracks from a given URL.
- `download_track_list(track_list, output_dir)`: Downloads a list of tracks to a specified output directory.
- `add_track_list_to_playlist(track_list, playlist_id)`: Adds a list of tracks to a given Spotify playlist.

### How to Use
- Run the script and provide the URL of the track list.
- Choose whether you want to download the tracks (d) or add them to a playlist (a).
- If you choose to download:
Enter the output directory where the tracks will be downloaded.
- If you choose to add to a playlist:
Enter the Spotify playlist ID to which the tracks will be added.
- The script will process the selected action and provide relevant output.

## Disclaimer
This script is provided as-is and might require further customization or adjustments based on your specific use case.

## License
This project is licensed under the MIT License.

## Contributions
Contributions are welcome! If you find any issues or want to enhance the functionality, feel free to open a pull request.

