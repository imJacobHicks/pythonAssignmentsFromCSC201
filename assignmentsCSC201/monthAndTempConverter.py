# Jacob Hicks - Assignment 9 Part 1

# PART 1 Month Number to Word Converter

# create a list for all numbers
# remember lists start at 0
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

print("-=( Month number to word converter )=- \n")

# start while loop
while True:
    try:
        number = int(input("Input number of month: "))

    except ValueError:  # allow loop to continue if user inputs an alpha character rather than an int by asking for an int input
        print("Please enter a valid number (1 through 12).")
        continue

    # number is not 1-12, so the user must input a corresponding number
    if number not in range(1, 13):
        print("Please enter a valid number (1 through 12).")
        continue

    elif number in range(1, 13):  # number is 1-12
        # define a variable to call later as an input of 1 would output February from the list because all lists start at 0
        listValue = number - 1
        # use the variable as the number to call the list value
        month = months[listValue]
        print(month)
        break


# PART 2 Farenheit to Celsius Converter

print("\n-=( Farenheit to Celsius Converter )=- \n")

while True:
    try:
        tempF = float(input("Temperature in F: "))

    except ValueError:  # allow loop to continue if user inputs an alpha character rather than a float by asking for a non alpha input
        print("Please enter a number, not a letter.")
        continue

    if True:
        tempC = (tempF - 32) * (5 / 9)
        print(f"{tempF :.2f} degrees F is {tempC :.2f} degrees C.")
        break

# prompt user for another
another = input("\nAnother conversion? (Y for Yes): ")

# while loop because user wants another
while another == "Y":
    try:
        tempF = float(input("Temperature in F: "))

    except ValueError:  # allow loop to continue if user inputs an alpha character rather than a float by asking for a non alpha input
        print("Please enter a number, not a letter.")
        continue

    if True:
        tempC = (tempF - 32) * (5 / 9)  # F to C conversion from Google
        # fromatting the temps two decimal places
        print(f"{tempF :.2f} degrees F is {tempC :.2f} degrees C.")
        # asking user if they want another to continue the loop or move to the if statement
        another = input("\nAnother conversion? (Y for Yes): ")
        continue

# user did not repsond Y, so we say our goodbyes
if another != "Y":
    print("Goodbye!")
