print("Thank you for choosing Python Pizza Deliveries!")
size = input("Input Size of Pizza (S/M/L): ")
add_pepperoni = input("Do you wish to add pepperoni? (Y/N): ")
extra_cheese = input("Do you wish to add extra cheese? (Y/N): ")

price = 0.0

if size.upper() == "S":
  price += 15.0
  if add_pepperoni.upper() == "Y":
    price += 2.0
elif size.upper() == "M":
  price += 20.0
  if add_pepperoni.upper() == "Y":
    price += 3.0
elif size.upper() == "L":
  if add_pepperoni.upper() == "Y":
    price += 3.0
  price += 25
  
if extra_cheese.upper() == "Y":
  price += 1.0

print(f"Your final bill is: ${price}")
  