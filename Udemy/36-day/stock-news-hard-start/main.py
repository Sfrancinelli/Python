import requests
from api_key import trading_api, news_api, ACCOUNT_SID, AUTH_TOKEN
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

time_now = datetime.now()
date_now = time_now.date()
print(date_now)

yesterday = datetime.today() - timedelta(days=1)
yesterday_date = str(yesterday.date())
print(yesterday_date)

day_after = datetime.today() - timedelta(days=2)
after_date = str(day_after.date())
print(after_date)

response = requests.get(STOCK_ENDPOINT, params={
    "symbol" : STOCK,
    "function" : "TIME_SERIES_DAILY_ADJUSTED",
    "apikey" : trading_api
})

response.raise_for_status()

data = response.json()

first_value = float(data['Time Series (Daily)'][after_date]['4. close'])
print(first_value)

later_value = float(data['Time Series (Daily)'][yesterday_date]['4. close'])
print(later_value)

percent_change = (later_value - first_value) / first_value * 100

up_down = None

if percent_change > 5:
    print("Get News")
elif percent_change < -5:
    print("-Get News")
else:
    print("Value hasn't changed by 5%")

if percent_change > 0:
    up_down = '⬆️'
else:
    up_down = '⬇️'

news_parameters = {
    "apiKey" : news_api,
    "q" : COMPANY_NAME,
    "from" : yesterday_date,
    "sortBy" : "relevancy",
    "pageSize" : 3
}

news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)

news_response.raise_for_status()

news_data = news_response.json()

print(news_data['articles'][0]['title'])
print(news_data['articles'][0]['description'])
print(news_data['articles'][1]['title'])
print(news_data['articles'][1]['description'])
print(news_data['articles'][2]['title'])
print(news_data['articles'][2]['description'])

three_articles = news_data['articles'][:3]
print(three_articles)

# [new_item for item in list]

formatted_article = [f"TSLA: {up_down}{round(percent_change)}\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

client = Client(ACCOUNT_SID, AUTH_TOKEN)

for article in formatted_article:
    message = client.messages.create(
        body=article,
        from_='+16018846323', 
        to="+54 11 3704 2581"
    )

    print(message.status)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

