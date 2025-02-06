# pcost.py
#
# Exercise 1.27

import os
import csv
import sys

def portfolio_cost(filename):
    f = open(filename,'rt')
    rows = csv.reader(f)
    next(f)

    total = 0

    for row in rows:
        try:
            price = float(row[-1])*float(row[-2])
            print(price)
            total += price
        except ValueError:
            print(f"Bad Row: {row}")

    f.close()
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = './Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost ${cost:0.2f}')