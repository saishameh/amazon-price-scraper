from bs4 import BeautifulSoup
import requests
import time
import datetime


def check_price():
    URL = 'https://www.amazon.ca/Insulated-Stainless-Bottles-Stickers-BPA-Free/dp/B0B8HMWPZ6/ref=sr_1_10?keywords=bottle&qid=1705972600&sr=8-10&th=1'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",  "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup_one = BeautifulSoup(page.content, "html.parser")

    soup_two = BeautifulSoup(soup_one.prettify(), "html.parser")

    ProductTitle = soup_two.find(id='productTitle').get_text()

    ProductPrice = soup_two.find(id='priceblock_ourprice').get_text()

    ProductPrice = ProductPrice.strip()[1:]
    ProductTitle = ProductTitle.strip()

    import datetime

    today = datetime.date.today()
    
    import csv 

    header = ['Title', 'Price', 'Date']
    data = [ProductTitle, ProductPrice, today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
 
    
# Runs check_price after a set time and inputs data in CSV

while(True):
    check_price()
    time.sleep(86400)