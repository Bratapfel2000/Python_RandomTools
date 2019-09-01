#roll the dice

#takes numbers 1-6 and picks them randomly for an specific amount of times.
#adds results together and calculates percentages

from random import choice

numbers = [i for i in range(1,7)]

k = 0
m = 0
n = 0
o = 0
p = 0
q = 0

for i in range(600):
    selection = choice(numbers)
    if selection == 1:
        k += 1
    if selection == 2:
        m += 1
    if selection == 3:
        n += 1
    if selection == 4:
        o += 1
    if selection == 5:
        p += 1
    if selection == 6:
        q += 1
        
x = k+m+n+o+p+q
print("No. x   %")
print("1", k, k*100/x)
print("2", m, m*100/x)
print("3", n, n*100/x)
print("4", o, o*100/x)
print("5", p, p*100/x)
print("6", q, q*100/x)
