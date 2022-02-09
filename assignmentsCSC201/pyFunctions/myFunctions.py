def calc_average():
    # Define Variable grade and grades
    grades = []

    # specify range of 5 for 5 iterations through the For loop
    for g in range(5):
        gradeNum = g + 1
        # int the input as it is stored as a string
        grade = int(input(f"Test Grade {gradeNum}: "))
        # cast input  to a tuple
        grades = [grade]

    avg = sum(grades) / len(grades)

    return avg


def determine_grade(avg):
    # if/else statement using avg variable from above to determine letter grade
    if avg <= 100 and avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"

    return grade
