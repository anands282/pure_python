print("Thankyou for choosing python pizza deliveries")
size = input("# What size pizza do you want? S, M, or L")
add_pepperoni = input("# Do you want pepperoni? Y or N ")
extra_cheese = input("# Do you want extra cheese? Y or N ")
base_amount = 0
pepperoni_amount = 0
cheese_amount = 0
if size == "S" and add_pepperoni == "Y":
    base_amount = 15
    pepperoni_amount = 2
elif size == "M" and add_pepperoni == "Y":
    base_amount = 20
    pepperoni_amount = 3
elif size == "L" and add_pepperoni == "Y":
    base_amount = 25
    pepperoni_amount = 3

if cheese_amount == "Y":
    cheese_amount = 1

print(f"Your final bill is: ${base_amount+pepperoni_amount+cheese_amount}")