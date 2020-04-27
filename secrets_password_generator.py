import secrets

number = int(input("enter length of password >>"))

print(secrets.token_hex(number))
