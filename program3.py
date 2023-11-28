penny_amount = 1
nickel_amount = 5
dine_amount = 10
quater_amount = 25
Total_amount_in_cents = 100

x = int(input("No. of pennies: "))
y = int(input("No. of nickles: "))
z = int(input("No. of dines: "))
w = int(input("No. of quaters: "))

coins_in_total = (x*penny_amount) + (y*nickel_amount) + (z*dine_amount) + (w*quater_amount)

Final_amount = coins_in_total / Total_amount_in_cents

if Final_amount == 1:
    print("Congratulations! The amount you entered was exactly one DOLLAR!")
    print("YOU WON....!!!!!!")
elif Final_amount < 1:
    print("Sorry, the amount you entered was LESS than one dollar.")
    print("BETTER LUCK NEXT TIME.....!!")
else:
    print("Sorry, the amount you entered was MORE than one dollar.")
    print("BETTER LUCK NEXT TIME.....!!")