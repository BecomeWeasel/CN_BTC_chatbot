#!/usr/bin/env python

import requests
import json
import csv
import os

from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

import telepot
from telepot.loop import MessageLoop
from pprint import pprint


# fill up your code!

class bithumb:
    def __init__(self, target_coin):
        self.target_coin = target_coin

        # self.target_coin
        # payload={'status'
        #          ,'data':{'average_price:'}}


bithumbUrl = "https://api.bithumb.com/public/ticker/BTC"

bitfinexUrl = "https://min-api.cryptocompare.com/data/price"
bitfinexParams = {'fsym': 'BTC', 'tsyms': 'USD', 'e': 'Bitfinex'}

R_bithumb = requests.post(bithumbUrl)
BTC_bithumb = json.loads(
    R_bithumb.text)  # R_bithumb.text ===str , so using json.loads, convert R_bithumb.text into dict format and assign to BTC_bitnumb(===dict)

R_bitfinex = requests.post(bitfinexUrl, params=bitfinexParams)
BTC_bitfinex = json.loads(R_bitfinex.text)

######
# if BTC_bithumb["status"] is '0000':
#     print("something wrong in bithumb tradecenter. or illegal requests.")
# print(BTC_bithumb["status"])

print(BTC_bithumb)

print(BTC_bitfinex)

print("%d" % float((BTC_bithumb["data"]["average_price"])))
