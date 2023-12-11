from pic_art import treasure
print(treasure)


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

a = input('''You're at a cross road. Where do you want to go? Type "left" or "right"\n''').lower()

if a == "left":
    b = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if b == "wait":
        c = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
        if c == "red":
            print("Burned by fire.Game over.")
        elif c == "blue":
            print("Eaten by beasts. Game Over.")
        elif c == "yellow":
            print("You found the treasure. You  Win!")
        else:
            print("Game Over")
    else:
        print("Attacked by trout. Game over.")
else:
    print("Fall into a hole. Game Over.")

