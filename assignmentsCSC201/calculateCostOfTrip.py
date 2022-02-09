# Jacob Hicks - Assignment 6

# importing tabulate module
from tabulate import tabulate

# Creating a function to omit negative values because you cannot go a negative speed


def nonNegativeInput(prompt):
    while True:
        try:
            value = float(input(prompt))  # stored as float to allow decimals
        except ValueError:
            # response to value error triggered by alpha inputs
            print(f"Sorry, this should be a number.")
            continue
        if value <= 0:
            # rule for inputs less than or equal to 0
            print(f"Sorry, this cannot be negative.")
            continue
        else:
            # input was sucessful and satisfies our requests
            break
    return value


# defining variables and asking for user input in the global scope
speed = nonNegativeInput("How fast are you driving in miles per hour? ")
hoursTraveled = nonNegativeInput("How many hours will you be traveling? ")
MPG = nonNegativeInput("How many miles does your car get per gallon? ")
pricePerGallon = nonNegativeInput(
    "What is the average cost for a gallon of gas? ")

# using global scope to make lists to append
hoursList = []
distanceList = []
gallonsList = []
costList = []

# showing user their input
print(f"\nSpeed in miles per hour: {int(speed)}")
print(f"Hours traveled: {int(hoursTraveled)}")
print(f"Miles per gallon: {int(MPG)}")
print(f"Price of gas per gallon: ${pricePerGallon:.2f}\n")


# while loop
while True:
    if hoursTraveled != 0:
        # create loop while hours travelled is not 0
        # nonNegativeInput function stores as float, so changing to an int
        hoursTraveling = int(hoursTraveled)
        # nonNegativeInput function stores as float, so changing to an int
        distance = int(hoursTraveled * speed)
        # rounding with format(number, '.2f')
        gallons = float(format((distance / MPG), '.2f'))
        # rounding with format(number, '.2f')
        cost = float(format(((distance / MPG) * pricePerGallon), '.2f'))

        # redfine hours traveled to continue loop
        hoursTraveled = hoursTraveled - 1

        # appending list AKA storing values
        hoursList.append(hoursTraveling)
        distanceList.append(distance)
        gallonsList.append(gallons)
        costList.append(cost)

    else:
        # sorting the list created above
        hoursList.sort()
        distanceList.sort()
        gallonsList.sort()
        costList.sort()

        # using tabulate to create a table
        # assigning column headers using headers = "keys" after creating dictionary/names tuple
        print(tabulate({"Hours": hoursList, "Distance": distanceList,
              "Gallons": gallonsList, "Cost": costList}, headers="keys"))

        break
