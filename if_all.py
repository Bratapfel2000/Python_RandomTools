"""
-gives out True if all items are the same
-False if one is different
-example only with lists
"""

fields = []
for i in range(9):
    fields.append(1)
    

def full():
    if all(fields):
        print("all true")
        print(all(fields))
    else:
        print("at least one false")
        print(all(fields))

print("")
print(type(fields))
print("")

print(fields)
full()

print("")
print("zero added")
print("")
fields.append(0)
print(fields)

full()

