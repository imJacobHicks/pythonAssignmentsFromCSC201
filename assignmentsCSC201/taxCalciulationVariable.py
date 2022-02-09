# Assignment 10 - Jacob Hicks

state_tax_rate = .05
county_tax_rate = .01

# Write your two functions here


def main():
    purchase_price = float(input("Purchase price: "))

    # Call your functions here and save their output to variables
    stateTax = purchase_price * state_tax_rate
    countyTax = purchase_price * county_tax_rate
    totalPrice = purchase_price + stateTax + countyTax

    # Output purchase price, state tax, county tax, and total
    print(f"Purchase price: {purchase_price:,.2f}")
    print(f"State tax: {stateTax:,.2f}")
    print(f"County tax: {countyTax:,.2f}")
    print(f"Total: {totalPrice:,.2f}")
    # See assignment instructions for required output format


main()
