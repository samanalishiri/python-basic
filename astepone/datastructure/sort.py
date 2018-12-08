from itertools import groupby
from operator import itemgetter

# Saman Alishiri samanalishiri@gmail.com


rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

sorted_rows = sorted(rows, key=lambda r: r['date'])
for row in sorted_rows:
    print(row)

rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for item in items:
        print(item)
