# pcost.py
#
# Exercise 1.27

import os
import csv
import sys

def portfolio_cost(filename):
    f = open(filename,'rt')
    rows = csv.reader(f)
    headers = next(rows)

    total = 0

    for rowno, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            nshares = int(record['shares'])
            price = float(record['price'])
            total += nshares * price
        except ValueError:
            print(f"Row {rowno}: Bad Row: {row}")

    f.close()
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = './Data/portfoliodate.csv'

cost = portfolio_cost(filename)

print(f'Total cost ${cost:0.2f}')