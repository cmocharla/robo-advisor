import json
import dotenv
import requests
import csv
import os

#TO DO 
#DATETIME 
#format to USD

#Accessing API 
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"

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



#breakpoint()





print("-------------------------")
print("SELECTED SYMBOL: XYZ")
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
print("HAPPY INVESTING!")
print("-------------------------")







# WRITING CSV 

# csv-mgmt/write_teams.py


csv_file_path = os.path.join(os.path.dirname(__file__), "data", "prices.csv")

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=["city", "name"])
    writer.writeheader() # uses fieldnames set above
    writer.writerow({"city": "NewYork", "name": "Yankees"})
    writer.writerow({"city": "New York", "name": "Mets"})
    writer.writerow({"city": "Boston", "name": "Red Sox"})
    writer.writerow({"city": "New Haven", "name": "Ravens"})
