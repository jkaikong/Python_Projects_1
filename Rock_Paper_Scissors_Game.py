
#Practice_2
#Rock Paper Scissors game

import random

print("Welcome to the Rock-Paper-Scissors Game!\n")
print("Here is the rule of this game:\n\n" +
"Rock VS Paper --> Paper wins\n" +
"Paper VS Scissors --> Scissors wins\n" +
"Scissors VS Rock --> Rock wins\n")


while True:
    print("Please choose a number: 1 for Rock, 2 for Paper, 3 for Scissors")
    choice = int(input())

    while (choice < 1) or (choice > 3):
        print("Please input a valid number: 1 for Rock, 2 for Paper, 3 for Scissors")
        choice = int(input())

    if choice == 1:
        player = "Rock"
    elif choice == 2:
        player = "Paper"
    elif choice == 3:
        player = "Scissors"
    print("You chose: " + player)

    ai = random.randint(1,3)
    if ai == 1:
        computer = "Rock"
    elif ai == 2:
        computer = "Paper"
    elif ai == 3:
        computer = "Scissors"
    print("The computer chose: " + computer)

    if (ai == 1 and choice == 2) or (ai == 2 and choice == 3) or (ai == 3 and choice == 1):
        print("Winner Winner, Chicken Dinner!")

    elif (ai == 2 and choice == 1) or (ai == 3 and choice == 2) or (ai == 1 and choice == 3):
        print("Game Over! You lose.")

    elif ai == choice:
        print("Tie Game!")

    print("Do you want to play again? (Y/N)")
    ans = input().upper()
    if ans == "N":
        break

print("\nThank you! See you next time.")
