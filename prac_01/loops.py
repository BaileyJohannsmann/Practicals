"""
CP1404 - Practical 1
Loops
Programs to demonstrate loops
"""
# print all the odd numbers between 1 and 20
for i in range(1, 20+1, 2):
    print(i, end=' ')
print()
# count in 10's from 0-100
for i in range(0, 100+1, 10):
    print(i, end=' ')
print()
# count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()
# Print number of stars
number_of_stars = int(input("Number of stars: "))
for i in range(1, number_of_stars+1):
    print('*', end=' ')
# Print n lines of increasing stars using the same input as above
for i in range(number_of_stars+1):
    print('*' * i)
    for j in range(number_of_stars):
        number_of_stars -= 1
print()
