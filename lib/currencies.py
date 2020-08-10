from pycoingecko import CoinGeckoAPI


def get_latest_btc(currency):
    cg = CoinGeckoAPI()

    return cg.get_price(ids='bitcoin', vs_currencies=currency)
