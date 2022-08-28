print("welcome to the tip caculator!")
bill = float(input ("what was the total bill? $"))
tip = int(input("how much tip would you like to give? 10, 12, or 15? "))
people = int(input("how many people to split the bill?"))
tips = tip / 100
total_tip = bill * tips
total_bill = total_tip + bill
bill_per = total_bill / people
finnal = round(bill_per, 2)
print(f"each person should pay {finnal}")