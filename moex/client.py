from datetime import datetime

import requests
import base64

from sqlalchemy import null

from db.models.companies import Companies
from db.models.stock_quotes import StockQuotes
from session import engine, SessionLocal, DatabaseSession

from fastapi import Depends
from sqlalchemy.orm import Session

from db.models.stocks import Stocks
from session import get_db, SessionLocal

# Specify the API endpoint URL
url = 'http://iss.moex.com/iss/history/engines/{engine}/markets/{market}/boards/{board}/securities.json'

# Specify the engine, market, board, and date for which you want to retrieve history securities
engine = 'stock'
market = 'shares'
board = 'tqbr'
date = '2023-05-17'

# Construct the complete URL with the parameters
complete_url = url.format(engine=engine, market=market, board=board)

# Set up authentication with MOEX Passport credentials
username = 'your_username'
password = 'your_password'
credentials = base64.b64encode((username + ':' + password).encode()).decode('utf-8')
headers = {'Authorization': 'Basic ' + credentials}

# Set up the request parameters
params = {'date': date}

# Send the API request
response = requests.get(complete_url, params=params)
# print(complete_url)
# print(params)
# print(datetime.utcnow())

# Check if the request was successful
if response.status_code == 200:
    # Process the response data (assuming it's in JSON format)
    data = response.json()
    # Process the data as needed
else:
    # Request was not successful
    print('Error:', response.status_code)


def match_metadata_and_data(metadata, data):
    matched_data = []

    for entry in data:
        matched_entry = {}
        for i, value in enumerate(entry):
            key = list(metadata.keys())[i]
            matched_entry[key] = value
        matched_data.append(matched_entry)

    return matched_data


def populate_database(data):
    # Вставка данных в базу данных
    with DatabaseSession() as session:


        for item in data:
            if item["LEGALCLOSEPRICE"] != null:
                stock = Stocks(company_symbol=item["SECID"],
                               company_name=item["SHORTNAME"],
                               stock_price=item["LEGALCLOSEPRICE"])
                session.add(stock)
        session.commit()
        for item in data:
            if item["LEGALCLOSEPRICE"] != null:
                if (item['VOLUME']==0):
                    stock_quotes = StockQuotes(stock_symbol=item["SECID"],
                                           date=item["TRADEDATE"],
                                           open_price=0,
                                            close_price=0,
                                           low_price=0,
                                           high_price=0,
                                           volume=0)
                else:
                    stock_quotes = StockQuotes(stock_symbol=item["SECID"],
                                           date=item["TRADEDATE"],
                                           open_price=item["OPEN"],
                                            close_price=item["CLOSE"],
                                           low_price=item["LOW"],
                                           high_price=item["HIGH"],
                                           volume=item["VOLUME"])
                session.add(stock_quotes)
        session.commit()
    print("Data inserted successfully")


print(populate_database(match_metadata_and_data(data['history']['metadata'], data['history']['data'])))
# print(match_metadata_and_data(data['history']['metadata'], data['history']['data']))
