import pandas
import numpy as np
import requests
import io
import urllib.request
from bs4 import BeautifulSoup
import csv
 
def main():
    klist=read_stock_data()
    for i in klist:
        get_dividents_nasdaq(i[0])

def get_dividents_nasdaq(symbol):
    url = "http://www.nasdaq.com/symbol/%s/dividend-history" % (symbol)
    result = urllib.request.urlopen(url)
    result = result.read()
    soup = BeautifulSoup(result,"lxml")
    si = soup.find("table", {"id": "quotes_content_left_dividendhistoryGrid"})    
    df = pandas.read_html(str(si))[0] 
    print(df)

def read_stock_data():
    with open('symbol.csv', 'r') as f:
        reader = csv.reader(f)
        klist = list(reader)
    return klist


if __name__ == '__main__':
    main()
