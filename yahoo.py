import requests
import numpy as np
import pandas as pd
from datetime import datetime, timedelta


def get_yahoo_data(ticker):
    raw_data = requests.get('https://query1.finance.yahoo.com/v7/finance/options/{}?formatted=true&crumb=okgpsvWZPzT&lang=en'
                        '-US&region=US&corsDomain=finance.yahoo.com'.format(ticker)).json()

    return raw_data


def get_expiration_dates(ticker):
    yahoo_data = requests.get('https://query1.finance.yahoo.com/v7/finance/options/{}?formatted=true&crumb=o'
                              'kgpsvWZPzT&lang=en-US&region=US&corsDomain=finance.yahoo.com'.format(ticker)).json()
    unix_dates = yahoo_data['optionChain']['result'][0]['expirationDates']
    add_days = [datetime.fromtimestamp(date) + timedelta(1) for date in unix_dates]
    formatted_dates = [date.strftime('%m-%d-%Y') for date in add_days]
    print(formatted_dates)
    return formatted_dates


def get_options_data(ticker, date, type):
    stock_data = requests.get('https://query1.finance.yahoo.com/v7/finance/options/{}?formatted=true&crumb=okgpsvWZPzT&'
                            'lang=en-US&region=US&date={}&corsDomain=finance.yahoo.com'.format(ticker, date)).json()
    drilled_data = stock_data['optionChain']['result'][0]['options'][0]

    for option in drilled_data[type]:
        option_data = {}
        keys = ['strike','lastPrice','bid','ask','volume','openInterest','impliedVolatility','lastTradeDate']
        for key in keys:
            if key in option:
                option_data[key] = option[key]['raw']
            else:
                option_data[key] = np.nan

        print(option_data)


def get_stock_data(ticker):
    yahoo_data = get_yahoo_data(ticker)
    if len(yahoo_data['optionChain']['result']) == 0:
        return None
    else:
        return yahoo_data['optionChain']['result'][0]['quote']





















