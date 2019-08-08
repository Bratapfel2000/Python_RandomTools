"""prints lines of textfile in a list"""

textfile = '.txt'


def word_lister(textfile):
    word_liste = []
    fin = open(textfile)
    for line in fin:
        word = line.strip()
        word_liste.append(word)
    return word_liste


print(word_lister(textfile))
