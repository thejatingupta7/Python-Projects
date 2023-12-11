print("Welcome to the tip Calculator")
a = float(input("What was the Total Bill? $"))
b = float(input("How many people to split the Bill? "))
c = float(input("What percentage tip would you like to give? 10, 12, or 15?"))
total = (a/b) + (((a*c)/100)/b)
total = round(total,2)
print(f"Each person should pay: {total}")


