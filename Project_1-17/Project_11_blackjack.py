# Blackjack Project
from pic_art import black_jack
print(black_jack)
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def deal_card():             # returns a random card
    import random
    cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards_deck)
    return card


user_cards = []
computer_cards = []
game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"users cards : {user_cards} & score = {user_score}")
    print(f"computer cards :{computer_cards} & score = {computer_score}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        ask = input("Do you want to draw another card? yes or no : ")
        if ask.lower() == "yes":
            user_cards.append(deal_card())
        else:
            game_over = True


def compare(user_score, computer_score):
    if computer_score == user_score:
        return "Draw."
    elif computer_score == 0:
        return "You lose, computer has a blackjack."
    elif user_score == 0:
        return "You win with a blackjack."
    elif user_score > 21:
        return "You lose."
    elif computer_score > 21:
        return "You win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."


while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(compare(user_score, computer_score))




