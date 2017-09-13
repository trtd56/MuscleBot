# -*- cording: utf-8 -*-

import falcon
import json
import requests

import datetime
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
from apscheduler.schedulers.blocking import BlockingScheduler

from twitter import tweet_search, oath_key_dict
import config

class CallbackResource(object):

    def on_post(self, req, resp):
        body = req.stream.read()
        receive_params = json.loads(body.decode('utf-8'))
        text = receive_params["events"][0]['message']["text"]

        reply_token = receive_params["events"][0]["replyToken"]

        if text == "筋肉":
            tweet = tweet_search(text, oath_key_dict)
            tweet_text = tweet['statuses'][0]['text']
            rep_text = "筋肉ニュースだよ！「" + tweet_text + "」"
            line_bot_api = LineBotApi(config.CHANNEL_ACCESS_TOKEN)
            try:
                line_bot_api.reply_message(reply_token, TextSendMessage(text=rep_text))
            except LineBotApiError as e:
                print(e)
        else:
            print(text)

api = falcon.API()
api.add_route('/callback', CallbackResource())
