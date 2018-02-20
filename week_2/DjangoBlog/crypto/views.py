from django.shortcuts import render

import requests

API = "https://api.coinmarketcap.com/v1/ticker/?limit=10"

def get_crypto(request):
    data = requests.get(API).json()
    ctx = {
        "data": data
    }
    return render(request, 'templates/crypto/crypto_currency.html', context=ctx)