# Jacob Hicks - Assignment 11

from myfunctions import *

# everything below provided by professor


def main():
    avg = calc_average()
    grade = determine_grade(avg)
    print(f"\nFinal Grade: {avg:.1f} ({grade})")


main()
