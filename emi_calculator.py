def calculate_emi(principal, annual_interest_rate, tenure_years):
    """
    Calculate the Equated Monthly Installment (EMI) for a loan.

    Parameters:
    principal (float): The loan amount.
    annual_interest_rate (float): The annual interest rate in percentage.
    tenure_years (float): The loan tenure in years.

    Returns:
    tuple: The monthly EMI, total interest payable, and total payment (principal + interest).
    """
    # Convert annual interest rate to a monthly rate
    monthly_interest_rate = annual_interest_rate / (12 * 100)

    # Convert tenure in years to months
    tenure_months = tenure_years * 12

    # Calculate EMI
    emi = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure_months) / \
          ((1 + monthly_interest_rate) ** tenure_months - 1)

    # Calculate total payment and total interest
    total_payment = emi * tenure_months
    total_interest = total_payment - principal

    return emi, total_interest, total_payment

def main():
    # Take inputs from the user
    principal = float(input("Enter the principal loan amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    tenure_years = float(input("Enter the loan tenure (in years): "))

    # Calculate EMI, total interest, and total payment
    emi, total_interest, total_payment = calculate_emi(principal, annual_interest_rate, tenure_years)

    # Print the results
    print(f"The EMI is: {emi:.2f}")
    print(f"Total interest payable is: {total_interest:.2f}")
    print(f"Total payment (principal + interest) is: {total_payment:.2f}")

if __name__ == "__main__":
    main()











*****************************************************************************************************************
def calculate_emi(principal, rate, time):
  """
  Calculates the EMI (Equated Monthly Installment) for a loan, total interest, and total payment.

  Args:
      principal: The loan amount (in rupees).
      rate: The annual interest rate (as a decimal).
      time: The loan duration in years.

  Returns:
      A tuple containing the monthly EMI amount (in rupees), total interest payable (in rupees), and total payment (in rupees).
  """

  # Convert annual interest rate to monthly rate
  monthly_rate = rate / 12 / 100

  # Calculate the number of monthly payments
  total_months = time * 12

  # Use the EMI formula to calculate the monthly payment
  emi = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** (-total_months))

  # Calculate total interest and total payment
  total_interest = emi * total_months - principal
  total_payment = emi * total_months

  return emi, total_interest, total_payment

# Get user input
principal = float(input("Enter the loan amount (in rupees): "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = float(input("Enter the loan duration (in years): "))

# Calculate EMI, total interest, and total payment
emi, total_interest, total_payment = calculate_emi(principal, rate, time)

# Print the results
print(f"The monthly EMI amount is: ₹{emi:.2f}")
print(f"The total interest payable is: ₹{total_interest:.2f}")
print(f"The total payment (principal + interest) is: ₹{total_payment:.2f}")

