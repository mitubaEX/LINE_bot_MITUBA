import sys,os
sys.path.append(os.pardir)
from data_store.spotify_store import SpotifyStore

class SpotifyRepository:
    def get_playlists(self, conf):
        return SpotifyStore(conf).get_playlists()
