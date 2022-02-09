# Jacob Hicks - Assignment 5
print("Let's check to see if you are eligible to set up and contribute to a Roth IRA account.\n")

# Creating a Function to ommit negative values and non-numerical characters


def nonNegativeInput(prompt):
    while True:  # creating while loop
        try:
            value = float(input(prompt))
        except ValueError:  # create a rule for alpha inputs resulting in a ValueError
            print(f"Sorry, this input should be a number.")
            continue
        if value <= 0:  # create a rule for inputs less than or equaL to 0
            print(f"Sorry, this input should be a number greater than 0.")
            continue
        else:
            # input was successfully parsed and we are happy with its value
            # ready to exit the loop now
            break
    return value


# asking for user input with the function created above that does not allow alpha or negative inputs
MAGI = nonNegativeInput("What is your mean adjusted gross income? ")
age = nonNegativeInput("How old are you? ")

# The above function (nonNegativeInput) ommits any value less than 0 and does not let the user proceed until a number greater than 0 is input. However, for sake of the assignment requirements I am using an 'or' operator
if MAGI <= 0 or MAGI >= 140000:  # rule for MAGI below 0 or above 140000
    # outputting multiple lines in one f-string with \n
    print(f"\nYour age: {int(age)} \nYour MAGI: {int(MAGI)} \n")
    # printing on a new line with a new print() looks cleaner imo
    print(f"You are not eligible to contribute to a Roth IRA.")

elif MAGI > 0 and MAGI < 6000:  # rule for MAGI between 0 and 6000
    # outputting multiple lines in one f-string with \n
    print(f"\nYour age: {int(age)} \nYour MAGI: {int(MAGI)} \n")
    # :, is used to add , to number, but it has to be outsite the int():, or you will get an error
    print(f"You may contribute up to ${int(MAGI):,} a year to your Roth IRA.")

elif MAGI > 125000 and MAGI < 140000:  # rule for MAGI between 125k and 140k
    # outputting multiple lines in one f-string with \n
    print(f"\nYour age: {int(age)} \nYour MAGI: {int(MAGI)} \n")
    # printing on a new line with a new print() looks cleaner imo
    print(f"You can make a partial contribution. Please check the IRS website for more information.")

else:
    if age < 50:  # rule for users under 50
        # outputting multiple lines in one f-string with \n
        print(f"\nYour age: {int(age)} \nYour MAGI: {int(MAGI)} \n")
        # printing on a new line with a new print() looks cleaner imo
        print(f"You may contribute up to $6,000 a year to your Roth IRA.")
    if age >= 50:  # rule for users above 50
        # outputting multiple lines in one f-string with \n
        print(f"\nYour age: {int(age)} \nYour MAGI: {int(MAGI)} \n")
        # printing on a new line with a new print() looks cleaner imo
        print(f"You may contribute up to $7,000 a year to your Roth IRA.")
