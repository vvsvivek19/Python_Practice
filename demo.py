total_income = float(input('Enter total income: '))
income_tax = 0

if total_income <= 300000:
    income_tax = 0
elif total_income <= 700000:
    income_tax = (total_income - 300000) * 0.05
elif total_income <= 1000000:
    income_tax = (400000 * 0.05) + (total_income - 700000) * 0.10
elif total_income <= 1200000:
    income_tax = (400000 * 0.05) + (300000 * 0.10) + (total_income - 1000000) * 0.15
elif total_income <= 1500000:
    income_tax = (400000 * 0.05) + (300000 * 0.10) + (200000 * 0.15) + (total_income - 1200000) * 0.20
else:
    income_tax = (400000 * 0.05) + (300000 * 0.10) + (200000 * 0.15) + (300000 * 0.20) + (total_income - 1500000) * 0.30

print("Income tax payable is", income_tax)
