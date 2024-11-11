# Input principal, rate, and time values
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
# Calculate compound interest
amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal
# Display the result
print("----------------------------")
print("The Compound Interest is: ",compound_interest)
print("The Total Amount is:",amount)
