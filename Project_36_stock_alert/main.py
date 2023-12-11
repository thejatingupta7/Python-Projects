import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "DSCDCTS2LA736EFA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

NEWS_API_KEY = "e22de4d8ec4a4a29acb1fa30008e454e"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]

yesterday_closing_price = data_list[0]['4. close']

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_closing_price = data_list[1]['4. close']

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference/float(yesterday_closing_price)) * 100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent > 4:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']
    top_three_articles = articles[:4]

    headline_description = [f"Headline: {article['title']}, \nBrief: {article['description']}" for article in top_three_articles]


#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. or by email
    import smtplib
    for headline in headline_description:
        my_email = "pycodedemon@gmail.com"
        password = "atlxhbcxjnbttzgo"
        send_to = "pycodedemon@yahoo.com"
        with smtplib.SMTP("smtp.gmail.com") as mail:
            mail.starttls()  # encrypt the email during transfer
            mail.login(user=my_email, password=password)
            mail.sendmail(
                from_addr=my_email,
                to_addrs=send_to,
                msg=f"Subject:Stocks Alert\n\n{headline}"
            )

#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

