# Jacob Hicks - Assignment 3

principal = float(input('What is your initial investment? '))

annualInterest = float(input('What is your annual interest rate? '))

investmentLength = int(
    input('How many years do you plan on accruing interest? '))

# turn percent into decimal
interest = annualInterest / 100

compoundInterest = 12

# compounding interest equation with created vars
returnOnInvestment = principal * \
    (1 + (interest / compoundInterest)) ** (compoundInterest * investmentLength)

# calculate the total profits
totalGrowth = returnOnInvestment - principal

# using int here to easily remove decimals rather than leaving the original var as a float
print(f"Principal investment: {int(principal)}")

print(f"Interest rate: {annualInterest}")

print(f"Years to invest: {investmentLength}")

# when using f-string:
# * you can round to a certain decimal point with var:.(desired decimal)f
# * you can also add commas to numbers with var:,
print(f"\nAfter {investmentLength} years at a rate of {annualInterest}% a year, your ${principal:,.2f} investment will be worth ${returnOnInvestment:,.2f}")

print(f"You will have earned ${totalGrowth:,.2f} on our initial investment.")
