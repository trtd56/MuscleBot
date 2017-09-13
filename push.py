# -*- cording: utf-8 -*-

import datetime
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
from apscheduler.schedulers.blocking import BlockingScheduler

import config

GYM_DAY = [0, 2, 5]  # 月, 水, 土
sched = BlockingScheduler()

def push_message():
    d = datetime.datetime.now()
    if d.weekday() in GYM_DAY:
        line_bot_api = LineBotApi(config.CHANNEL_ACCESS_TOKEN)
        try:
            line_bot_api.push_message(config.TO, TextSendMessage(text=config.MESSAGE))
        except LineBotApiError as e:
            print(e)

@sched.scheduled_job('cron', hour=7)
def timed_job():
    push_message()

sched.start()
