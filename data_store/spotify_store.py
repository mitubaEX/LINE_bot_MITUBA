import sqlalchemy as sa
from configure import Configure
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyStore:
    def __init__(self, conf):
        self.client_id = conf.spotify_client_id
        self.client_secret = conf.spotify_client_secret
        self.client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(self.client_id, self.client_secret)
        self.spotify = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)

    def get_playlists(self):
        self.result = self.spotify.featured_playlists(limit=5)
        return self.result['playlists']['items']
