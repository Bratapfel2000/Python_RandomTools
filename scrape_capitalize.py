#scrapes a word and capitalizises it/them


from bs4 import BeautifulSoup
import requests
import time
import random

#scrapes a word
source = requests.get('---').text
soup = BeautifulSoup(source, 'html.parser')
eins = soup.find(id="---")
zwei = eins.find_all(class_="---")
drei = zwei[0]
#print(drei.text)

#waehlt zufaellig gut oder schlecht aus +impor random
a = ["gut", "schlecht", "voll gut", "naja", "geht so", "spitzenklasse",
     "erste Sahne", "zweite Sahne", "voll Zehlendorf", "unangenehm", "gar nicht mal so gut",
     "besser", "schlechter", "hipstermaessig"]

#capitalize
print(drei.text.title() + " ist " + random.choice(a) + ".")   
