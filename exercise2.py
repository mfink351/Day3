height = input("Enter your height in meters: ")

weight = input("Enter your weight in kgs: ")

bmi = float(f"{(float(weight) / (float(height) ** 2) ):.2f}")

print(f"Your BMI is {bmi}")

if bmi <= 18.5:
  print("You are underweight.")
elif bmi > 18.5 and bmi <= 25:
  print("You are a normal weight.")
elif bmi > 25 and bmi <= 30:
  print("You are slightly overweight.")
elif bmi > 30 and bmi <= 35:
  print("You are obese.")
elif bmi > 35:
  print("You are chronically obese.")
elif bmi < 0:
  print("Invalid BMI.")
