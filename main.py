#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range (0, nr_letters): 
  password_list += random.choice(letters)

for char in range (0, nr_numbers): 
  password_list += random.choice(numbers)

for char in range (0, nr_symbols): 
  password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password if {password}")

#Not optimal solution 
'''
possible_characters = []
possible_characters.extend(letters)
possible_characters.extend(numbers)
possible_characters.extend(symbols)
characters_in_password = nr_letters + nr_symbols + nr_numbers

password = ""

for char in range (0, characters_in_password): 
  password += random.choice(possible_characters)

print(password)
'''

