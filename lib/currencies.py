from pycoingecko import CoinGeckoAPI

def get_latest_btc():
    cg = CoinGeckoAPI()

    return cg.get_price(ids='bitcoin', vs_currencies='eur')['bitcoin']['eur']
