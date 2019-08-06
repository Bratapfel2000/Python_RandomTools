"""with py3.7
adds items from a list to a dictionary
"""

known = {}
t = ['d', 'c', 'e', 'b', 'a']
print(known)

def dict_adder(t):
    for i in range(len(t)):
        known[i+1] = t[i]
        i += 1
    return known
        
        
dict_adder(t)


print(known)
