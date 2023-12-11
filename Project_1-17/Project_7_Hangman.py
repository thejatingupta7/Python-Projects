
from Project_7_resources import logo, stages
print(logo)

from Project_7_resources import word_list

import random
chosen_word = random.choice(word_list)
display =[]
for letter in chosen_word:
    display += "_"
print(display)

lives = 5

end_of_game = False

while not end_of_game:
    guess = input("Guess a  letter : ").lower()

    if guess in display:
        print("You've already guessed it!")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    if guess not in chosen_word:
        print("You chose wrong letter. You lose a live!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win!")


    print(stages[lives])


