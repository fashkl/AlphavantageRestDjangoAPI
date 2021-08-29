import os
from datetime import datetime

from requests import request
from decimal import Decimal
from .models import BitcoinToUSDRates
from constants import *


def get_bitcoin_usd_exchange_rate(*args, **kwargs):
    alpha_vantage_api_key = os.environ.get('ALPHA_VANTAGE_KEY')
    if not alpha_vantage_api_key:
        return False

    url = "https://www.alphavantage.co/query"
    headers = {
        CUSTOM_TOKEN_HEADER: CUSTOM_TOKEN,
    }
    querystring = {"function": "CURRENCY_EXCHANGE_RATE", "from_currency": "BTC",
                   "to_currency": "USD", "apikey": alpha_vantage_api_key}

    response = request("GET", url, headers=headers, params=querystring).json()

    if 'Error Message' in response:
        return False

    exchange_rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
    last_refreshed = response['Realtime Currency Exchange Rate']['6. Last Refreshed']

    if exchange_rate and last_refreshed:
        BitcoinToUSDRates(exchange_rate=Decimal(exchange_rate), last_refreshed=last_refreshed).save()
    else:
        return False

    return True
