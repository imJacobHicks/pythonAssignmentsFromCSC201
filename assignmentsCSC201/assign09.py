# Assignment #9 - Jacob Hicks

# Task 1: Print the variable below with
# a formatter of two decimal places,
# so that output is: 28.73
print("Task #1")
num = 28.73132
print(f"{num :.2f}")


# Task 2: Use an f-string format to print the variables
# below in the following format:
# Turlough Dobbins owes $1,325.88 in taxes.
first_name = "Turlough"
last_name = "Dobbins"
taxes = 1325.878
print("\nTask #2")
print(f"{first_name} {last_name} owes ${taxes :,.2f} in taxes.")


# Task 3: Using an if/else statement, output
# whether the input age is old enough to vote (18)
print("\nTask #3")
age = int(input("Age: "))
if age >= 18:
    print(
        f"Your age of {age} is old enough to vote because you are 18 years or older.")
else:
    print(f"Sorry, your age of {age} is not 18 or older, so you cannot vote.")


# Task 4: Using a single if/else statement, if the
# age is 12 and under or 65 and older, output
# "You get in free!", otherwise output: "Your ticket
# is regular price."
print("\nTask #4")
age = int(input("Age: "))
if age <= 12 or age >= 65:
    print(f"You get in free!")
else:
    print(f"Your ticket is regular price.")


# Task 5: Using if/elif/else, output whether the user
# types a positive number, a negative number, or zero.
print("\nTask #5")
num = int(input("Number: "))
if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print(f"{num} is 0.")


# Task 6: Write a while loop that outputs the
# numbers 1 through 10.
print("\nTask #6")
n = 0
while n < 10:
    n += 1
    print(n)


# Task 7: Write a for loop that outputs the
# numbers 5 through 10.
print("\nTask #7")
n = 5
for n in range(4, 10):
    n += 1
    print(n)


# Task 8: Given the list below, use a for loop to
# determine the average of the grades.
print("\nTask #8")
grades = [88, 95, 72, 87, 100]
total = 0

for g in grades:
    total = sum(grades)

print(total / len(grades))
