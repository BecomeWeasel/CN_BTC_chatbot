#!/usr/bin/env python

import requests
import json
import csv
import os

from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import locale
import telepot
from telepot.loop import MessageLoop
from pprint import pprint

locale.setlocale(locale.LC_ALL, '')


# fill up your code!
def GetBTC():
    Time = datetime.datetime.now()
    currentTime = Time.strftime('%Y-%m-%d %H:%M')
    print(currentTime)
    USD=GetBitfinex()
    KRW=GetBithumb()

    bot.sendMessage(455389867,"{0}\nBTC KRW is ₩ {1} from Bithumb\nBTC USD is $ {2} from Bitfinex".format(currentTime,KRW,USD))



def GetBithumb():
    bithumbUrl = "https://api.bithumb.com/public/ticker/BTC"
    R_bithumb = requests.post(bithumbUrl)
    BTC_bithumb = json.loads(
        R_bithumb.text)  # R_bithumb.text ===str , so using json.loads, convert R_bithumb.text into dict format and assign to BTC_bitnumb(===dict)
    return BTC_bithumb["data"]["average_price"]


def GetBitfinex():
    bitfinexUrl = "https://min-api.cryptocompare.com/data/price"
    bitfinexParams = {'fsym': 'BTC', 'tsyms': 'USD', 'e': 'Bitfinex'}
    R_bitfinex = requests.post(bitfinexUrl, params=bitfinexParams)
    BTC_bitfinex = json.loads(R_bitfinex.text)
    return BTC_bitfinex["USD"]


if __name__ == "__main__":
    bot = telepot.Bot('458359558:AAE3CSoLc67Y8-R7IT7deuuZB8qnL5NBct4')
    scheduler = BlockingScheduler()
    scheduler.add_job(GetBTC, 'interval', minutes=1)
    scheduler.start()
