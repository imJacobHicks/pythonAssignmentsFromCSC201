# Jacob Hicks - Assignment 2
pi = 3.14159
astronaut1 = 'Martian'
astronaut2 = 'Skywalker'
ship = 'Starship'
planet = "Pluto's Big Brother"
radius = 3000000  # really big
encounter = 'aliens'  # if they're lucky
home = 'Earth'

circ = (2 * pi) * radius

# using f-string for print requires {} around vars
# \n = new line \t = tab\indent
# format (AKA round to 'x' decimal points) is used as {var:.xf} f = format

print(f"Astronauts {astronaut1} and {astronaut2} were exploring space. \nThey were aboard the {ship} exploring the plaet {planet}.\n{planet} has a circumference of {circ:.2f} kilometers. \nOn the planet, they encountered {encounter} and ran back to the ship. \nThey blasted off in \n3... \n\t2... \n\t\t1... \n....and made it safely back to {home}. The end.")
