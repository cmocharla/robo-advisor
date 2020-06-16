
#Packages 

import dotenv

import json
import requests
import csv
import os
import datetime


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"(${my_price:,.2f})"  #> $12,000.71

t = datetime.datetime.now()
#import urllib.request #https://stackoverflow.com/questions/1949318/checking-if-a-website-is-up-via-python

from dotenv import load_dotenv
#Accessing API Key
load_dotenv()
os.getenv("ALPHAVANTAGE_API_KEY")

y = os.getenv("ALPHAVANTAGE_API_KEY")


#Validation of user input against length and numeric values
while True:
        x = input(
            "PLEASE ENTER A STOCK SYMBOL:")
        if len(x) < 10:
            pass
        else:
            print("Symbol Too Long")
        if x.isdigit() is False:
            pass
        else:
           print("CONTAINS NUMBER TRY AGAIN")
        try:
            request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={x}&apikey={y}"
            response = requests.get(request_url)
            parsed_response = json.loads(response.text)
            #last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
            break
        except KeyError:
            print("STOCK NOT FOUND")
  


#Short Cut for Time Series Daily
tsd = parsed_response["Time Series (Daily)"]

#List of Dates 
dates = list(tsd.keys())
latest_day = dates[0]
latest_closing = tsd[latest_day]["4. close"]
f_latest_closing = float(latest_closing)

#High And Low Price Lists 
high_prices = []
low_prices = []

#Looping Through Dates and accessing prices to create high and low variables and lists. 
for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)
f_recent_high = recent_high
f_recent_low = recent_low
symbol = parsed_response["Meta Data"]['2. Symbol']


# WRITING CSV 

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
csv_file_path = os.path.join(os.path.dirname(__file__), "data", "prices.csv")

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above

    for date in dates:
        daily_prices = tsd[date]


        
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]
            })



#Recomendations
if float(latest_closing) < float(recent_high):
    advice = "Buy"
else:
    advice = "SELL"


if float(latest_closing) < float(recent_high):
    reason = "LAST CLOSING LOWER THAN RECENT HIGH"
else:
    reason = "LAST CLOSING HIGHER THAN RECENT HIGH"


print("-------------------------")
print(f"SELECTED SYMBOL: {symbol}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: " + (t.strftime("%Y-%m-%d %I:%M %p")))
print("-------------------------")
print(f"LATEST DAY: {latest_day}")
print(f"LATEST CLOSE: {to_usd(f_latest_closing)}")
print(f"RECENT HIGH: {to_usd(f_recent_high)}")
print(f"RECENT LOW: {to_usd(f_recent_low)}")
print("-------------------------")
print(f"RECOMMENDATION: {advice}!")
print(f"RECOMMENDATION REASON: {reason}")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")




