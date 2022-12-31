import pandas as pd
import requests

url = "https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY"
headers = {
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

session = requests.Session()

data = session.get(url, headers=headers).json()["records"]["data"]

ocdata = []

for i in data:
    for j, k in i.items():
        if j=="PE" or j=="CE":
            info = k
            info["Instrument Type"] = j
            ocdata.append(info)

def refinedata (exp = "05-Jan-2023"):
    df = pd.DataFrame(ocdata)
    df.drop(["underlying","change","pChange","bidQty","bidprice","askQty","askPrice","identifier"],axis=1,inplace=True)
    indexprice = df["underlyingValue"][2]
    df = df[(df["strikePrice"] >= indexprice-600) & (df["strikePrice"] <= indexprice+600)]
    df = df[df["expiryDate"] == exp]
    return df







