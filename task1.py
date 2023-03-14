# Input
investment_amount = float(input("Investment Amount: "))
monthly_payment_amount = float(input("Monthly Payment Amount: "))
annual_interest_rate = float(input("Annual Interest Rate: "))
number_of_years = float(input("Number of Years: "))

# Fixes values
annual_interest_rate /= 100
monthly_interest_rate = annual_interest_rate / 12
number_of_months = number_of_years * 12

# Calculates and rounds future value
future_value = investment_amount * ((1+ monthly_interest_rate)**number_of_months) + monthly_payment_amount * ((((1 + monthly_interest_rate)**number_of_months) - 1) / monthly_interest_rate) * (1 + monthly_interest_rate)
future_value = round(future_value, 2)

# Prints value
print(future_value)