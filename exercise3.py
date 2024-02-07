year = int(input("Please enter a year: "))

if year % 4 == 0 and year % 100 == 0:
  if year % 400 == 0:
    print("It is a leap year.")
  else:
    print("It is not a leap year.")
else:
  print("It is not a leap year.")