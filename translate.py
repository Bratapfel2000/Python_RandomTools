import string

punkt = string.punctuation
print(punkt)
firstString = punkt
secondString = len(punkt)*" "
#thirdString = "ab"

string = "aha!aha-aha+aha-aha+aha-aha%aha)aha/aha%aha?aha*aha/aha"
print("Original string:", string)

translation = string.maketrans(firstString, secondString) #,thirdString)

# translate string
print("Translated string:", string.translate(translation))

