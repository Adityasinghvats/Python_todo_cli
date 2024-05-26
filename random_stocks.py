import requests

def fetch_random_stock():
    url = "https://api.freeapi.app/api/v1/public/stocks/stock/random"
    stocks = requests.get(url)
    fetched_stocks = stocks.json()

    if fetched_stocks["success"] and "data" in fetched_stocks:
        data = fetched_stocks ["data"]
        name = data["Name"]
        symbol = data["Symbol"]
        marketcap = data["MarketCap"]
        currentprice = data["CurrentPrice"]
        dividendyield = data["DividendYield"]
        facevalue = data["FaceValue"]
        return name,symbol,marketcap,currentprice,dividendyield,facevalue
    else:
        raise Exception("Failed to get data!")

def main():
    try:
        stock_name,symbol,marketcap,currentprice,dividendyield,facevalue = fetch_random_stock()
        print(f"Stock Name:{stock_name}\nSymbol:{symbol}\nMarketcap:{marketcap}\nCurrentprice:{currentprice}\nDividendyield:{dividendyield}\nFacevalue:{facevalue}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()

        