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
    Time=datetime.datetime.now()
    currentTime = Time.strftime('%Y-%m-%d %H:%M')
    print(currentTime)
    GetBitfinex()
    GetBithumb()


def GetBithumb():
    bithumbUrl = "https://api.bithumb.com/public/ticker/BTC"
    R_bithumb = requests.post(bithumbUrl)
    BTC_bithumb = json.loads(
        R_bithumb.text)  # R_bithumb.text ===str , so using json.loads, convert R_bithumb.text into dict format and assign to BTC_bitnumb(===dict)
    print("BTC KRW is ₩ %.3d from Bithumb" % float(BTC_bithumb["data"]["average_price"]))

def GetBitfinex():
    bitfinexUrl = "https://min-api.cryptocompare.com/data/price"
    bitfinexParams = {'fsym': 'BTC', 'tsyms': 'USD', 'e': 'Bitfinex'}
    R_bitfinex = requests.post(bitfinexUrl, params=bitfinexParams)
    BTC_bitfinex = json.loads(R_bitfinex.text)
    print("BTC USD is $ %.3d from Bitfinex" % float(BTC_bitfinex["USD"]))


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(GetBTC, 'interval', minutes=1)
    scheduler.start()
