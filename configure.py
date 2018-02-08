import sys
import os

class Configure:
    def __init__(self):
        # get channel_secret and channel_access_token from your environment variable
        self.channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
        self.channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
        if self.channel_secret is None:
            print('Specify LINE_CHANNEL_SECRET as environment variable.')
            sys.exit(1)
        if self.channel_access_token is None:
            print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
            sys.exit(1)

        # get twitter config
        self.spotify_client_id = os.getenv('SPOTIFY_CLIENT_ID', None)
        self.spotify_client_secret = os.getenv('SPOTIFY_CLIENT_SECRET', None)
        if self.spotify_client_id is None:
            print('Specify SPOTIFY_CLIENT_ID as environment variable.')
            sys.exit(1)
        if self.spotify_client_secret is None:
            print('Specify SPOTIFY_CLIENT_SECRET as environment variable.')
            sys.exit(1)
