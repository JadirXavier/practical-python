# pcost.py
#
# Exercise 1.27

import os

f = open('./Data/portfolio.csv','rt')
next(f)

total = 0

for line in f:
    row = line.replace('\n','').split(',')
    price = float(row[-1])*float(row[-2])
    print(price)
    total += price

print(f'Total cost ${total:0.2f}')

f.close()