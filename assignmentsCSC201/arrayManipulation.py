# Jake Hicks - Assignment 12

# create a list of months by name
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

# empty list for data which is to be input by user
rainfallData = []

# prompt user to input data for rainfall
print("Input total rainfall for each month:")

# for loop that iterates 12 times, one for each month
for m in range(12):
    # define m from list of months
    month = months[m]
    # call variable that specifies month by name in prompt
    rainfall = float(input(f"{month} rainfall (cm): "))
    # append the input data to the list
    rainfallData.append(rainfall)
    # increase m by 1 each iteration to get all months
    m += 1

# **sort the data from smalled to largest
rainfallData.sort()

# variable that adds all data in list
totalRainfall = sum(rainfallData)

# variable that uses an equation to get the average of the list of data
averageRainfall = sum(rainfallData) / len(rainfallData)

# variables for max and min of rainfall using the indexes. **Note that the list is sorted globally above
maxRainfall = rainfallData[-1]
minRainfall = rainfallData[0]

# print summary in format specified by the assignment
print("\nRainfall data summary\n")

print(f"Total rainfall: {totalRainfall:.2f}")
print(f"Average rainfall: {averageRainfall:.2f}")
print(f"Max rainfall: {maxRainfall:.2f}")
print(f"Min rainfall: {minRainfall:.2f}")
