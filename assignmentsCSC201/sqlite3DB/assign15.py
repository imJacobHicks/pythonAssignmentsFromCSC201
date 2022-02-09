import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

query = ""

# Query # 1
#		 Select name and capital of all countries with
# 	 greater than 100,000,000 population, from largest
#		 to smallest
query = "SELECT name, population FROM world WHERE population >= 100000000 ORDER BY population DESC"

# Create query, execute, and fetch results here
bigCountries = cursor.execute(query).fetchall()

print("--=-=-=( Countries with 100-million+ People )=-=-=--")
# Loop through and output results here
for query in bigCountries:
    print(*query)


# Query # 2
#		 Select name and area of the FIVE smallest countries, from
#		 smallest to largest
query = "SELECT name, area FROM world ORDER BY population ASC LIMIT 5 "
# Create query, execute, and fetch results here
fiveSmallestCountries = cursor.execute(query).fetchall()
print("\n--=-=-=( Five Smallest Countries )=-=-=--")

# Loop through and output results here

for query in fiveSmallestCountries:
    print(f"{query} km\u00b2")


# Query # 3
#		 Select names of all countries that start with
# 	 the characters entered by the user

print("\n--=-=-=( Country Name Search )=-=-=--")
chars = input("Beginning characters of country name: ")

# Create query, execute, and fetch results here
query = (f"SELECT name FROM world WHERE name LIKE '{chars}%'")

result = cursor.execute(query).fetchall()
# If any results were returned, loop through and output results here. Otherwise output 'not found' message text from requirements.

if result != None:
    for query in result:
        print(query)
    else:
        print("Not found")

conn.close()
