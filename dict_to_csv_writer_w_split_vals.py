'''
saves dict to csv with splitted values
'''

import csv

textfile= 'file.csv'

mydict = {0: ['eins', 'one', 0, 0],
          1: ['zwei', 'two', 0, 0],
          2: ['drei', 'three', 0, 0],
          3: ['vier', 'four', 0, 0]}
     
with open('file.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in mydict.items():
       writer.writerow([key, value[0], value[1], value[2], value[3]])
       print([key, value[0], value[1], value[2], value[3]])

