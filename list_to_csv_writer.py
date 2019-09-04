import csv

textfile= 'file.csv'

myData = [["eins","one","0"],["zwei","two","0"]]

myFile = open(textfile, 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     
