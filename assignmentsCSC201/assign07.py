# Jacob Hicks - Assignment 7

# create list as instructed
grades = [100, 58, 87, 76, 60]

for g in range(5):
    grade = grades[g]  # variable for grade in print

    # if, elif, else statement to determine letter grade based on percentage
    if grade <= 100 and grade >= 90:
        gradeLetter = "A"
    elif grade < 90 and grade >= 80:
        gradeLetter = "B"
    elif grade < 80 and grade >= 70:
        gradeLetter = "C"
    elif grade < 70 and grade >= 60:
        gradeLetter = "D"
    else:
        gradeLetter = "F"

    # keeping print statement in FOR loop so it prints 5 times as defined by the range
    # g+1 makes the range 1-5 rather than 0-4 because all lists start at 0
    print(f"Quiz #{g+1}:\t{grade} ({gradeLetter})")

# Outside of FOR loop

# variable and equation for average of lists
average = sum(grades) / len(grades)
# if, elif, else statement to determine letter grade for average grade
if average <= 100 and average >= 90:
    avgLetter = "A"
elif average < 90 and average >= 80:
    avgLetter = "B"
elif average < 80 and average >= 70:
    avgLetter = "C"
elif average < 70 and average >= 60:
    avgLetter = "D"
else:
    avgLetter = "F"

print(f"\nAverage Grade: {average} ({avgLetter})")
