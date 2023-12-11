from pic_art import rock,paper,scissors

choices = [rock, paper, scissors]

# User Chose
user = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.\n"))
if user == 0 or user == 1 or user == 2:
    print(choices[user])
else:
    print("invalid input")


# computer chose
print("Computer chose: ")
import random
computer = random.randint(0, 2)
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)


# Who won????
if user == 0 and computer == 1:
    print("You lose.")
elif user == 0 and computer == 2:
    print("You won.")
elif user == 1 and computer == 0:
    print("You won.")
elif user == 1 and computer == 2:
    print("You lose.")
elif user == 2 and computer == 0:
    print("You lose.")
elif user == 2 and computer == 1:
    print("You won.")
elif user > 2:
    print("You chose invalid value. You lose!")
else:
    print("Its a tie.")
