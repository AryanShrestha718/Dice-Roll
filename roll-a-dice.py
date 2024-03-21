from random import randint


answer = ""
answer = input("Would you like to roll a dice? Y/N")
for i in answer != "y":
    answer = input("Would you like to roll a dice? Y/N")
number = randint(1,6)

if number == 1:
    print("|-----|")
    print("|     |")
    print("|  o  |")
    print("|     |")
    print("|-----|")
if number == 2:
    print("|-----|")
    print("|    o|")
    print("|     |")
    print("|o    |")
    print("|-----|")
if number == 3:
    print("|-----|")
    print("|    o|")
    print("|  o  |")
    print("|o    |")
    print("|-----|")
if number == 4:
    print("|-----|")
    print("|o   o|")
    print("|     |")
    print("|o   o|")
    print("|-----|")
if number == 5:
    print("|-----|")
    print("|o   o|")
    print("|  o  |")
    print("|o   o|")
    print("|-----|")
if number == 6:
    print("|-----|")
    print("|o   o|")
    print("|o   o|")
    print("|o   o|")
    print("|-----|")