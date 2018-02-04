import os
import sys
from argparse import ArgumentParser
from repository.user_repository import UserRepository
from repository.money_repository import MoneyRepository
from model.user import User
from model.money import Money
from services.tweet import Tweet
from configure import Configure

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

conf = Configure()
line_bot_api = LineBotApi(conf.channel_access_token)
handler = WebhookHandler(conf.channel_secret)

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

@app.route("/not", methods=['GET'])
def notification():
    # handle webhook body
    try:
        push_message()
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    # get user profile
    profile = line_bot_api.get_profile(event.source.user_id)

    # insert user profile to database
    UserRepository().add_user(User(profile.display_name,
                                    profile.user_id,
                                    profile.picture_url,
                                    profile.status_message))
    message = event.message.text

    # '円使った'という文字が見えたら，そこから数字を抽出してDBに保存
    if '円使った' in message:
        int_message = message.replace('円使った', '')
        if int_message.isdigit():
            moneyRepository = MoneyRepository()

            # add_money
            moneyRepository.add_money(Money(event.timestamp, int(int_message)))

            # get_money
            for row in moneyRepository.get_money():
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text='君の残高は今{0}だよ'.format(row[2]))
                )
        else:
            # varidation
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='数値入力して？')
            )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )

def push_message():
    Tweet().tweet(conf)

if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)

