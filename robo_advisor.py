import json
import dotenv
import requests
import csv
import os

from dotenv import load_dotenv

load_dotenv()

#TO DO 
#DATETIME 
#format to USD

#Accessing API 
x = "IBM"
os.getenv("ALPHAVANTAGE_API_KEY")

y = os.getenv("ALPHAVANTAGE_API_KEY")



request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={x}&apikey={y}"



response = requests.get(request_url)
#print(type(response))
#print(response.status_code)
#print(response.text)

# Parsing Response Via JSON 
parsed_response = json.loads(response.text)
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"] 

#Short Cut for Time Series Daily
tsd = parsed_response["Time Series (Daily)"]

#List of Dates 
dates = list(tsd.keys())
latest_day = dates[0]
latest_closing = tsd[latest_day]["4. close"]

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

symbol = parsed_response["Meta Data"]['2. Symbol']

#breakpoint()


# WRITING CSV 

# csv-mgmt/write_teams.py

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
csv_file_path = os.path.join(os.path.dirname(__file__), "data", "prices.csv")

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above

    #looping 
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


#
    ##looping 
    #writer.writerow({
    #    "timestamp": "TODO",
    #    "open": "TODO",
    #    "high": "TODO",
    #    "low": "TODO",
    #    "close": "TODO",
    #    "volume": "TODO"
    #    })




print("-------------------------")
print(f"SELECTED SYMBOL: {symbol}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {latest_closing}")
print(f"RECENT HIGH: {recent_high}")
print(f"RECENT LOW: {recent_low}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")






