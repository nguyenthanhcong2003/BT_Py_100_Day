years = int(input("Which do you want to check: "))

if years % 4 == 0:
  if years % 100 == 0:
    if years % 400 == 0:
      print ("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
  