import yfinance as yf
import json
ticker = "TSLA"

tckr = yf.Ticker(f"{ticker}")
response = tckr.info

v = json.dumps(response, indent=4)
# get stock info
with open(f"{ticker}.txt", "w") as file:
    file.write(v)
    file.close()
    print(v)


# https://pypi.org/project/yfinance/
