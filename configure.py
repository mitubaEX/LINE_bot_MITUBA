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

