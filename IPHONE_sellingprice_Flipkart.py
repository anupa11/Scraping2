# Let us work through an example of web scraping the price information off of a flipkart page.

import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.flipkart.com/apple-iphone-12-pro-max-pacific-blue-128-gb/p/itmd89812b558a03').text
soup = BeautifulSoup(r, 'lxml')
# print(soup.prettify())
match1 = soup.find('div', class_='_30jeq3 _16Jk6d')
# print(match1)
match2 = match1.text
print(f'The current selling price of APPLE iPhone 12 Pro Max (Pacific Blue, 128 GB) on Flipkart is: {match2}')