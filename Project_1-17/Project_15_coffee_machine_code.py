from Project_15_coffee_data import MENU
from pic_art import coffee
resources = {"Water": 300, "Milk": 200, "Coffee": 100, "Money": 0}

print(coffee)

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    def resource_sufficient():
        global count
        count = 0
        if resources["Water"] <= MENU[choice]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            count += 1
        elif resources["Milk"] <= MENU[choice]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            count += 1
        elif resources["Coffee"] <= MENU[choice]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee powder.")
            count += 1
        else:
            pass

    if choice == "off":
        break
    elif choice == "report":
        for i, j in resources.items():
            if i == "Water" or i == "Milk":
                print(f"{i}: {j}ml")
            elif i == "Coffee":
                print(f"{i}: {j}g")
            else:
                print(f"{i}: ${j}")
    else:
        resource_sufficient()

        if count != 0:
            continue

        print("Please insert coins.")
        m1 = int(input("How many quarters?: "))
        m2 = int(input("How many dimes?: "))
        m3 = int(input("How many nickels?: "))
        m4 = int(input("How many pennies?: "))
        total = (m1*0.25)+(m2*0.10)+(m3*0.05)+(m4*0.01)

        for i in MENU:
            if i == choice:
                if total < MENU[i]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    print(f"Here is ${total - MENU[i]['cost']} in change.")
                    print(f"Here is your {choice}☕ enjoy!")
                    resources["Water"] -= MENU[choice]["ingredients"]["water"]
                    resources["Milk"] -= MENU[choice]["ingredients"]["milk"]
                    resources["Coffee"] -= MENU[choice]["ingredients"]["coffee"]
                    resources["Money"] += MENU[choice]["cost"]

