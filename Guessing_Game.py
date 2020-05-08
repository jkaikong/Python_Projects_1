#Project_1
#Guess the number

import random

count = 0
n = random.randint(0, 30)

while count < 5:
    x = int(input("Please guess a number: "))
    count += 1

    if x == n:
        print("Congratulations! You Win!")
        break
    elif x < n:
        print("Sorry, your guess is too small. Please try again.")
    elif x > n:
        print("Sorry, your guess is too high. Please try again.")

if not count < 5:
    print("Sorry, you lose. The correct number is:",n)
