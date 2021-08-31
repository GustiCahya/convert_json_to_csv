# !/usr/bin/env python2.7

import json
import unicodecsv as csv

with open('data.json','rb') as fin:
    data = json.load(fin)

with open('data.csv','wb') as csv_file:
    w = csv.writer(csv_file, encoding='utf-8')
    w.writerow(data[0].keys())  # header row
    for row in data:
        w.writerow(row.values())