import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "RKYFNF5Q5ZBQ8CNS"
# https://newsapi.org/
# Use twilio.com/docs/sms/quickstart/python

stockParams = {
    "function": "TIME_SERIES_DAILY", "symbol": STOCK_NAME, "apikey": STOCK_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=stockParams)
data = response.json()["Time Series (Daily)"]
dataList = [value for (key, value) in data.items()]
yesterdayData = dataList[0]
yesterdayClosingPrice = yesterdayData["4. close"]
print(yesterdayClosingPrice)

dayBeforeYesterdayData = dataList[1]
dayBeforeYesterdayClosingPrice = dayBeforeYesterdayData["4. close"]
print(dayBeforeYesterdayClosingPrice)

difference = abs(float(yesterdayClosingPrice) - float(dayBeforeYesterdayClosingPrice))
print(difference)

diffPercent = (difference / float(yesterdayClosingPrice)) * 100
print(diffPercent)

if diffPercent > 5:
    print("Get news")
