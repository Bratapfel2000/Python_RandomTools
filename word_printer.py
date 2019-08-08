"""prints lines of textfile"""

textfile = '.txt'

def words_printer(textfile):
    fin = open(textfile)
    for line in fin:
        word = line.strip()
        print(word)

words_printer(textfile)
