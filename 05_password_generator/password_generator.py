import random

print("Welcome To Password Generator")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
number = int(input("Amount of passwords to generate: "))
length = int(input("Input your password length: "))
print("\nHere are your passwords: ")

for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
