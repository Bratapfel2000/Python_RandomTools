"""makes a dictionary out of a list"""


textfile = '.txt'

def word_lister(txtfile):
    word_liste = []
    fin = open(txtfile)
    for line in fin:
        word = line.strip()
        word_liste.append(word)
    return word_liste


def word_dictmaker(txtfile):
    word_liste = word_lister(txtfile)
    worter_dikt = {}
    for i in range(len(word_liste)):
        worter_dikt[i] = word_liste[i]
    return worter_dikt

print(word_dictmaker(textfile))
