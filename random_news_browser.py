"""
created with python 3.7
"""

import random
import webbrowser

link_list = """text file with list of links"""

"""creates a list out of text file"""
def linkliste():
    fin = open(link_list)
    liste = []
    for line in fin:
        word = line.strip()
        liste.append(word)
    return liste

"""takes link list and choses n random pages to open in browser"""
def random_opener(n):
    liste = linkliste()
    y =  random.sample(liste,n)
    for i in y:
        webbrowser.open_new_tab(i)

random_opener(5)



