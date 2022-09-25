"""
CP1404 - Practical 1
Shop Calculator
Program to calculate shop item costs and apply discount if value in a certain range
"""
total = 0
number = int(input("Number of items: "))
while number < 0:
    print("Number of items is invalid")
    number = int(input("Number of items: "))
for i in range(number):
    price = float(input("Cost of item: "))
    total += price
if total > 100:
    total *= 0.9
print("Total price for {} items is ${:.2f}".format(number, total))
