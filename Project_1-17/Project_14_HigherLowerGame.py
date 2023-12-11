from ../pic_art import higherlower, vs
from Project_14_game_data import data
from random import randint


score = 0
game_over = True


while game_over:
    guess1 = data[randint(0, 49)]
    guess2 = data[randint(0, 49)]
    if guess1["follower_count"] == guess2["follower_count"]:
        continue
    print(higherlower)
    print("Compare A:", guess1['name'], ",", guess1["description"], ", from", guess1["country"])
    print(vs)
    print("Compare B:", guess2['name'], ",", guess2["description"], ", from", guess2["country"])

    if score != 0:
        print(f"You're right! Current score: {score}")

    user = input("Who has more followers? Type 'A' or 'B' : ").upper()
    if user == 'A':
        if guess1["follower_count"] > guess2["follower_count"]:
            score += 1
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = False
    elif user == 'B':
        if guess2["follower_count"] > guess1["follower_count"]:
            score += 1
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = False
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = False






