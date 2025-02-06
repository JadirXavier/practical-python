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

l = read_prices(filename)

pprint(l)