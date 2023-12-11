from pic_art import calculator
print(calculator)

"""
num1 = float(input("What's the first number?: "))
print('''+
-
*
/''')
operator = input("Pick an operator: ")
num2 = float(input("What's the next number?: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print("Wrong input for operator.")

print(f"{num1} {operator} {num2} = {result}")
"""


# making calculator using functions and dictionary
def calculator():
    print('''           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_| 
 ''')

    def add(num1, num2):
        return num1+num2
    def minus(num1, num2):
        return num1-num2
    def multiply(num1, num2):
        return num1*num2
    def divide(num1, num2):
        return num1/num2

    operators = {'+':add,
                '-':minus,
                '*':multiply,
                '/':divide
                }

    num1 = float(input("What's the first number?: "))
    for i in operators:
        print(i)
    ask = True
    while ask:
        operator = input("Pick an operator: ")
        num2 = float(input("What's the next number?: "))

        symbol = operators[operator]
        result = symbol(num1,num2)

        print(f"{num1} {operator} {num2} = {result}")

        num1 = result

        if input(f"If you want to continue with the {result}, enter 'yes', otherwise 'no': ") == 'no':
            ask = False


calculator()