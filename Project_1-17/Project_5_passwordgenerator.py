# Password Generator Project

print("Welcome to the PyPassword Generator!")
a = int(input("How many letters would you like in your password?\n"))
b = int(input("How many symbols would you like?\n"))
c = int(input("How many numbers would you like?\n"))

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Easy Level
'''
password_list = ""
for i in range(1, a + 1):
    random_letter = random.choice(letters)
    password_list += random_letter

for i in range(1, b + 1):
    password_list += random.choice(symbols)

for i in range(1, c + 1):
    password_list += random.choice(numbers)

print(password_list)'''



# Hard Level


password_list = []
for i in range(1, a + 1):
    random_letter = random.choice(letters)
    password_list += random_letter

for i in range(1, b + 1):
    password_list += random.choice(symbols)

for i in range(1, c + 1):
    password_list += random.choice(numbers)

print(password_list)                        # password in list form
random.shuffle(password_list)               # shuffle() function
print(password_list)                        # password shuffled

password = ""
for i in password_list:
    password += i                           # converting list into string

print(f"Your password is: {password}")
