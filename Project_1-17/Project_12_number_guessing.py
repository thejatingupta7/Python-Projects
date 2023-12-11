import pic_art
import random
print(pic_art.number_guessing_game)
print("\nWelcome to the Number guessing game!\nI'm thinking of a number between 1 and 100. ")


difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ")
if difficulty == 'easy':
    n = 10
else:
    n = 5

number = random.randint(1, 101)

while n > 0:
    print(f"You have {n} attempts remaining to user_guess the number.")
    guess = int(input("Make a user_guess: "))
    if guess == number:
        print("You guessed it correctly!")
        break
    elif guess > number:
        print("Too High!")
    elif guess < number:
        print("Too Low!")
    else:
        print("invalid!")
    n -= 1
else:
    print("You Lose! ,You've run out of chances.")