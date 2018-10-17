number = input('Enter Number 1: ')
number2 = input('Enter Number 2: ')
n = int(number)
m = int(number2)
print("The Number is: " + number)
print("The Number is: " + number2)

if n % m == 0:
    print(n, 'divides evenly by ', m)
else:
    print(n, 'does not divides evenly by ', m)
    
if n % 4 == 0:
    print('divideable by 4')
elif n % 2 == 0:
    print('Number 1 is even')

else:
    print('Number 1 is odd')
