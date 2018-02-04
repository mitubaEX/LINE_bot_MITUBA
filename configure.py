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
        self.twitter_consumer_key = os.getenv('TWITTER_CONSUMER_KEY', None)
        self.twitter_consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET', None)
        self.twitter_access_token = os.getenv('TWITTER_ACCESS_TOKEN', None)
        self.twitter_access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET', None)
        if self.twitter_consumer_key is None:
            print('Specify TWITTER_CONSUMER_KEY as environment variable.')
            sys.exit(1)
        if self.twitter_consumer_secret is None:
            print('Specify TWITTER_CONSUMER_SECRET as environment variable.')
            sys.exit(1)
        if self.twitter_access_token is None:
            print('Specify TWITTER_ACCESS_TOKEN as environment variable.')
            sys.exit(1)
        if self.twitter_access_token_secret is None:
            print('Specify TWITTER_ACCESS_TOKEN_SECRET as environment variable.')
            sys.exit(1)
