

def readMyFile(filename):
    x = []
    y = []
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            x.append(row[0])
            y.append(row[1])
    return lang1, lang2
x,y = readMyFile(vocabulary_file)

