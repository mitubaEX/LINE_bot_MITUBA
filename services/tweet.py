import json
import requests
from requests_oauthlib import OAuth1Session

class Tweet():
    def tweet(self, conf):
        self.twitter_consumer_key = conf.twitter_consumer_key
        self.twitter_consumer_secret = conf.twitter_consumer_secret
        self.twitter_access_token = conf.twitter_access_token
        self.twitter_access_token_secret = conf.twitter_access_token_secret

        url = 'https://api.twitter.com/1.1/statuses/update.json'

        auth = OAuth1Session(self.twitter_consumer_key, self.twitter_consumer_secret, self.twitter_access_token, self.twitter_access_token_secret)
        r = auth.post(url, params={"status":"Hello"})

        if r.status_code == 200: #スターテスコードの確認
            print ("connect succeed!")
        else:
            print ("Error: %d" % r.status_code)
