import requests


def fetch_instrument_key_from_symbol(symbol):
    instrument_key = ""
    import upstox.instruments as instruments
    for stocks in instruments.instruments:
        if stocks["trading_symbol"] == symbol.upper() and stocks["segment"] == "NSE_EQ":
            instrument_key = stocks["instrument_key"]
            break
    return instrument_key


def fetch_historical_candle_data(symbol, interval, to_date, from_date):
    try:
        instrument_key = fetch_instrument_key_from_symbol(symbol)
        if not instrument_key:
            return {"err": "Incorrect Symbol"}
        url = "https://api.upstox.com/v2/historical-candle/{}/{}/{}/{}".format(
            instrument_key, interval, to_date, from_date)
        headers = {
            'Accept': 'application/json'
        }
        response = requests.request("GET", url, headers=headers)
        return response.json()
    except Exception as e:
        return {"err": str(e)}
