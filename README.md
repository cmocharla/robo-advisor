# robo-advisor

In order to run this program please 


## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

## Set UP
### Environment Setup and Requirements 

Create and activate a new Anaconda virtual environment:


conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env

From within the virtual environment, install the required packages specified in the "requirements.txt" file.


pip install -r requirements.txt

## Security Requirements

This program will need an API Key to issue requests to the [AlphaVantage API](https://www.alphavantage.co). But the program's source code should absolutely not include the secret API Key value. Instead, you should set an environment variable called `ALPHAVANTAGE_API_KEY`, and your program should read the API Key from this environment variable at run-time.

Use a "dotenv" approach to setting project-specific environment variables by using a file called ".env" in conjunction with [the `dotenv` package](/notes/python/packages/dotenv.md). Example ".env" contents:

```
ALPHAVANTAGE_API_KEY="abc123"
```

Use gitignore to ignore the .env file 

API https://www.alphavantage.co/


## Sub Folder
Create a sub folder
CSV 

