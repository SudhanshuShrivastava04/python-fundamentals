sip = float(input("Enter Monthly SIP Amount: "))
months = int(input("Enter Time Period (in months): "))
expected_interest = float(input("Enter monthly expected interest rate (%): "))

estimated_amount = 0.0
total_invested = 0.0
monthly_rate = expected_interest / 100   

for month in range(1, months + 1):

    total_invested += sip
    estimated_amount += sip

    estimated_amount += estimated_amount * monthly_rate

    print(
        f"After {month} months: "
        f"Estimated Amount = {estimated_amount:.2f}, "
        f"Total Invested = {total_invested:.2f}"
    )

print("\nInvestment Time Period Completed!\n")

gain = estimated_amount - total_invested
gain_percent = (gain / total_invested) * 100 if total_invested != 0 else 0

print(f"Total Invested: {total_invested:.2f}")
print(f"Estimated Amount: {estimated_amount:.2f}")
print(f"Total Gain: {gain:.2f}")
print(f"Gain %: {gain_percent:.2f}%")
