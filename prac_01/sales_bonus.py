"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
HIGH_BONUS_RATE = 0.15
LOW_BONUS_RATE = 0.1
BONUS_THRESHOLD = 1000

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= BONUS_THRESHOLD:
        bonus = HIGH_BONUS_RATE
    else:
        bonus = LOW_BONUS_RATE
    print(f"Your bonus is {sales * bonus: .2f}$")
    sales = float(input("Enter sales: $"))
print("Farewell")
