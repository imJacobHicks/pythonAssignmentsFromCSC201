# Jacob Hicks - Assignment 13

# variable asking user for amount of names in list
amount = int(input("How many names will be on your list? "))

# open write command with "W"
names = open("names.txt", "w")

for line in range(amount):

    # line automatically starts at 0, so add 1
    # create a variable to call in user input prompt
    num = line + 1
    # create variable for user input
    name = input(f"Name {num}: ")
    # adds 1 to every input looping through until range 5 is met
    num += 1

    # write names to variable that globally stores text file
    names.write(name + "\n")

print("\nNames from file:")

# close write command
names.close()

# create new variable for names in names txt file and reading with "r"
inNames = open("names.txt", "r")

# for loop through all names (each "line") in txt file
for line in inNames:
    # formatting with f-line concatenation to tab each name as the assignment format asks
    print(f"\t{line.strip()}")

# close read command
inNames.close()
