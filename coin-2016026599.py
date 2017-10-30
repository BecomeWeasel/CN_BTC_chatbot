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


# fill up your code!
def GetBTC():
    Time = datetime.datetime.now()
    currentTime = Time.strftime('%Y-%m-%d %H:%M')
    print(currentTime)
    USD = GetBitfinex()
    KRW = float(GetBithumb())
    KRW_MOVE = 0
    USD_MOVE = 0
    prevValues = []
    currentKRWValues = []
    currentUSDValues = []
    isInitial = True
    READ = open('BTC.csv', 'r+')
    reader = csv.reader(READ, delimiter=',')
    for row in reader:
        if (row != None):
            prevValues.append(row)
            isInitial = False
        else:
            break
    READ.close()

    currentKRWValues.append(str(KRW))
    currentUSDValues.append(str(USD))

    if isInitial is False:
        KRW_MOVE = float(currentKRWValues[0]) - float(prevValues[0][0])
        USD_MOVE = float(currentUSDValues[0]) - float(prevValues[1][0])

    WRITE = open('BTC.csv', 'w')
    writer = csv.writer(WRITE, quotechar=',', delimiter=',')
    writer.writerow(currentKRWValues)
    writer.writerow(currentUSDValues)

    WRITE.close()

    bot.sendMessage(455389867,
                    "{0}\nBTC KRW is ₩ {1}\nChange : {2} from Bithumb\nBTC USD is $ {3}\nChange : {4} from Bitfinex".format(
                        currentTime, KRW, KRW_MOVE, USD, USD_MOVE))


def GetBithumb():
    bithumbUrl = "https://api.bithumb.com/public/ticker/BTC"
    R_bithumb = requests.post(bithumbUrl)
    BTC_bithumb = json.loads(
        R_bithumb.text)
    return BTC_bithumb["data"]["average_price"]


def GetBitfinex():
    bitfinexUrl = "https://min-api.cryptocompare.com/data/price"
    bitfinexParams = {'fsym': 'BTC', 'tsyms': 'USD', 'e': 'Bitfinex'}
    R_bitfinex = requests.post(bitfinexUrl, params=bitfinexParams)
    BTC_bitfinex = json.loads(R_bitfinex.text)
    return BTC_bitfinex["USD"]


if __name__ == "__main__":
    bot = telepot.Bot('458359558:AAE3CSoLc67Y8-R7IT7deuuZB8qnL5NBct4')
    directory = os.getcwd()
    directory += "/BTC.csv"
    if not os.path.exists(directory):
        csvfile = open("BTC.csv", 'w+')
        csvfile.close()
    scheduler = BlockingScheduler()
    scheduler.add_job(GetBTC, 'interval', minutes=1)
    scheduler.start()
