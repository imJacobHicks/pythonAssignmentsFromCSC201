# Jake Hicks - Assignment 4

# Ask for user input on length and width of rectangles
# Float the input to allow for decimal input
print(f"Please enter the units in feet. They will be converted into meters after the calculations are done.\n")

# Creating a Function to ommit negative values and non-nuimerical characters


def nonNegativeInput(prompt):
    while True:  # creating while loop
        try:
            value = float(input(prompt))
        except ValueError:  # create a rule for non-numerical inputs resulting in a ValueError
            print(f"Sorry, I only understand numerical inputs.")
            continue
        if value <= 0:  # create a rule for inputs less than or equaL to 0
            print(f"Sorry, your response must not be negative or 0.")
            continue
        else:
            # input was successfully parsed and we are happy with its value
            # ready to exit the loop now
            break
    return value


L1 = nonNegativeInput("Enter Rectangle 1 length: ")
W1 = nonNegativeInput("Enter Rectangle 1 width: ")
L2 = nonNegativeInput("Enter Rectangle 2 length: ")
W2 = nonNegativeInput("Enter Rectangle 2 width: ")

# equations for area using vars
area1 = L1 * W1
area2 = L2 * W2

# convert areas from feet to meters
area1Meters = float(area1 * 0.3048)
area2Meters = float(area2 * 0.3048)

# more f-string print formatting with {var:,.2f} below
#:, to add commas to numbers
#:.2f to format/round to 2 decimal points

if area1 == area2:
    print(
        f"\nRectangle 1 and Rectangle 2 both have the same area of {area1:,.2f} feet.")
    # display areas in meters
    print(f"\nArea of Rectangles in meters: {area1Meters:,.2f} meters")

elif area1 < area2:
    print(
        f"\nRectangle 1 has an area of {area1:,.2f} feet which is less than the Rectangle 2 area of {area2:,.2f} feet.")
    # display areas in meters
    print(
        f"\nRectangle 2: {area2Meters:,.2f} meters \nRectangle 1: {area1Meters:,.2f} meters")

elif area1 > area2:
    print(
        f"\nRectangle 1 has an area of {area1:,.2f} feet which is greater than the Rectangle 2 area of {area2:,.2f} feet.")
    # display areas in meters
    print(
        f"\nRectangle 1: {area1Meters:,.2f} meters \nRectangle 2: {area2Meters:,.2f} meters")
