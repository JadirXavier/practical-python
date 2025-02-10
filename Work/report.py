# report.py
#
# Exercise 2.4

from pprint import pprint
import csv
import sys
import os

'''
def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(f)
        for row in rows:
            try:
                portfolio.append({'name':row[0], 'shares': int(row[1]), 'price': float(row[2])})
            except ValueError:
                print(f"Bad Row {row}")

    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = './Data/portfolio.csv'

l = read_portfolio(filename)

pprint(l)

'''

'''
def read_prices(filename):

    stocks = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(f)
        for row in rows:
            try:
                if row == []:
                    continue
                stocks[row[0]] = float(row[1])
            except ValueError:
                print(f"Bad Row {row}")
    return stocks

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = './Data/prices.csv'

def make_report(data):
    

l = read_prices(filename)


print(f'l')
'''

def make_report(portfolio, price):
    stocks = []
    prices = {}

    with open(portfolio, 'rt') as f:
        rows = csv.reader(f)
        next(f)
        for row in rows:
            try:
                stocks.append({'name':row[0], 'shares': int(row[1]), 'price': float(row[2])})
            except ValueError:
                print(f"Bad Row {row}")

    with open(price, 'rt') as f2:
        rows = csv.reader(f2)
        for row in rows:
            try:
                if row == []:
                    continue
                prices[row[0]] = float(row[1])
            except ValueError:
                print(f"Bad Row {row}")
    
    report = []

    for dict in stocks:
        if dict['name'] in prices:
            report.append((dict['name'], dict['shares'], prices[dict['name']], prices[dict['name']] - dict['price']))
        else:
            continue
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- -----------')
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {f"${price:.2f}":>10s} {change:>10.2f}')

make_report('./Data/portfolio.csv','./Data/prices.csv')

