
# We’ll scrape the current stock price of GOOG from yahoo finance and create a function to get the current price live. 

# https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch

import requests
from bs4 import BeautifulSoup
import datetime
def PriceTracker():
    r = requests.get('https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch').text
    soup = BeautifulSoup(r, 'lxml')
    match1 = soup.find('div', class_='D(ib) Mend(20px)')
    match2 = match1.span.text
    return match2
while True:
    print(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} Current stock price of GOOG is ${PriceTracker()}')
    

 


