import os
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

# Set environment variables for your Spotify app
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:3000'  # For this script, a redirect URI isn't required.

# Define the scope for accessing the currently playing track
SCOPE = 'user-read-playback-state'

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))
def get_currently_playing():
    # Get the current playback information
    current_playback = sp.current_playback()

    if current_playback is None:
        print("No song is currently playing.")
        return

    # Get song details
    song_name = current_playback['item']['name']
    artist_name = ', '.join(artist['name'] for artist in current_playback['item']['artists'])
    duration_ms = current_playback['item']['duration_ms']
    playback = {
        'artist': artist_name,
        'song': song_name,
        'duration_ms': duration_ms
    }
    return playback

if __name__ == "__main__":
    get_currently_playing()
