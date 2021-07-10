
# We’ll scrape the current stock price of AAPL from yahoo finance and create a function to get the current price live. 

# https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch

import requests
from bs4 import BeautifulSoup
import datetime
def PriceTracker():
    r = requests.get('https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch').text
    soup = BeautifulSoup(r, 'lxml')
    # print(soup.prettify())
    match1 = soup.find('div', class_='D(ib) Mend(20px)')
    # print(match1)
    match2 = match1.span.text
    return match2
timeStamp = datetime.datetime.now()
timeStamp = timeStamp.strftime("%Y-%m-%d %H:%M:%S")
while True:
    print(f'{timeStamp} Current stock price of AAPL is ${PriceTracker()}')


# Alternatively, we can use the find_all method:

# import requests
# from bs4 import BeautifulSoup
# r = requests.get('https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch').text
# soup = BeautifulSoup(r, 'lxml')
# # print(soup.prettify())
# match1 = soup.find_all('div', class_='D(ib) Mend(20px)')
# # print(match1[0])
# match2 = match1[0].span.text
# print(f'Current stock price of AAPL is ${match2}')


 


