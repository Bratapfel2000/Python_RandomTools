import random

def generator():
    strength = int(input("Enter length of password: "))
    big_letters = []
    small_letters = []
    stuff = []
    for i in range(65,91):
        big_letters.append(chr(i))
    for i in range(97,123):
        small_letters.append(chr(i))
    for i in range(33,65):
        stuff.append(chr(i))

    div_three = strength // 3
    am_big = div_three
    am_small = div_three
    am_stuff = strength-am_big-am_small
    password_pot = []

    for x in range(am_big):
        password_pot.append(random.choice(big_letters))
    for x in range(am_small):
        password_pot.append(random.choice(small_letters))
    for x in range(am_stuff):
        password_pot.append(random.choice(stuff))

    random.shuffle(password_pot)
    password = ''
    for letter in password_pot:
        password += letter
    print("Generated Password:", password)

if __name__ == "__main__":
    generator()

    
