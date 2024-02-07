name1 = input("Enter name one: ")
name2 = input("Enter name two: ")
combo = name1.upper() + name2.upper()

tCount = combo.count("T")
rCount = combo.count("R")
uCount = combo.count("U")
e1Count = combo.count("E")
trueCount = tCount + rCount + uCount + e1Count

lCount = combo.count("L")
oCount = combo.count("O")
vCount = combo.count("V")
e2Count = combo.count("E")
loveCount = lCount + oCount + vCount + e2Count

loveScore = int(str(trueCount) + str(loveCount))


print("The Love Calculator is calculating your score...")
if loveScore < 10 or loveScore > 90:
  print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore <= 50:
  print(f"Your score is {loveScore}, you are alright together.")
else:
  print(f"Your score is {loveScore}.")






