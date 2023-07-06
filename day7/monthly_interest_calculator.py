def main():
    print("This a monthly payment loan calculator")
    print("")

    principal = float(input("Enter the loan amount: "))
    apr = float(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of years: "))

    monthly_interest_rate = apr/1200
    number_or_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-number_or_months))
    total_payment = monthly_payment * number_or_months
    print("***************************************************")
    print("The monthly payment for this loan : shs. %.2f  " % monthly_payment)
    print("The total amount that will be paid : shs. %.2f  " % total_payment)

main()

print([e for e in range(100) if e%2==0
    ])
