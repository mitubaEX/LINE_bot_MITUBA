import os
import sys
from argparse import ArgumentParser
from configure import Configure

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn
)

app = Flask(__name__)

conf = Configure()
line_bot_api = LineBotApi(conf.channel_access_token)
handler = WebhookHandler(conf.channel_secret)

client_id = conf.spotify_client_id
client_secret = conf.spotify_client_secret
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    if 'プレイリスト' in event.message.text:
        playlists = get_playlists()
        colums_list = [ CarouselColumn(
            thumbnail_image_url=i['images'][0]['url'],
            title=i['name'],
            text='playlist',
            actions=[
                URITemplateAction(
                    label='Go',
                    uri=i['external_urls']['spotify']
                    )
                ]
            ) for i in playlists ]
        carousel_template_message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=colums_list
            )
        )
        line_bot_api.reply_message(
            event.reply_token,
            carousel_template_message
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )

def get_playlists():
    result = spotify.featured_playlists(limit=5)
    return result['playlists']['items']

if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)

