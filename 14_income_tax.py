total_income = float(input('Enter total income: '))
income_tax = 0
first_bucket = 0
second_bucket = 0
third_bucket = 0
fourth_bucket = 0
fifth_bucket = 0
sixth_bucket = 0
rebate = 20000
if total_income <= 300000:
    income_tax = 0
    print("Income tax payable is",income_tax)
else:
    first_bucket = 300000
    second_bucket = total_income - first_bucket
    if second_bucket <= 400000:
        income_tax = (first_bucket * 0) + second_bucket * 0.05
        print("Income tax payable is",income_tax)
    else:
        first_bucket = 300000
        second_bucket = 400000
        third_bucket = total_income - first_bucket - 400000
        if third_bucket <= 300000:
            income_tax = (first_bucket * 0) + second_bucket * 0.05 + third_bucket * 0.10 - rebate
            print("Income tax payable is",income_tax)
        else:
            first_bucket = 300000
            second_bucket = 400000
            third_bucket = 300000
            fourth_bucket = total_income - first_bucket - second_bucket - third_bucket
            if fourth_bucket <= 200000:
                income_tax = (first_bucket * 0) + second_bucket * 0.05 + third_bucket * 0.10 + fourth_bucket * 0.15 - - rebate
                print("Income tax payable is",income_tax)
            else:
                first_bucket = 300000
                second_bucket = 400000
                third_bucket = 300000
                fourth_bucket = 200000
                fifth_bucket = total_income - first_bucket - second_bucket - third_bucket - fourth_bucket
                if fifth_bucket <= 300000:
                    income_tax = (first_bucket * 0) + second_bucket * 0.05 + third_bucket * 0.10 + fourth_bucket * 0.15 + fifth_bucket * 0.20 - rebate
                    print("Income tax payable is",income_tax)
                else: 
                    first_bucket = 300000
                    second_bucket = 400000
                    third_bucket = 300000
                    fourth_bucket = 200000
                    fifth_bucket = 300000
                    sixth_bucket = total_income - first_bucket - second_bucket - third_bucket - fourth_bucket - fifth_bucket
                    income_tax = (first_bucket * 0) + second_bucket * 0.05 + third_bucket * 0.10 + fourth_bucket * 0.15 + fifth_bucket * 0.20 + sixth_bucket * 0.30 - rebate
                    print("Income tax payable is",income_tax)

# Another method

# total_income = float(input('Enter total income: '))
# income_tax = 0

# if total_income <= 300000:
#     income_tax = 0
# elif total_income <= 700000:
#     income_tax = (total_income - 300000) * 0.05
# elif total_income <= 1000000:
#     income_tax = (400000 * 0.05) + (total_income - 700000) * 0.10
# elif total_income <= 1200000:
#     income_tax = (400000 * 0.05) + (300000 * 0.10) + (total_income - 1000000) * 0.15
# elif total_income <= 1500000:
#     income_tax = (400000 * 0.05) + (300000 * 0.10) + (200000 * 0.15) + (total_income - 1200000) * 0.20
# else:
#     income_tax = (400000 * 0.05) + (300000 * 0.10) + (200000 * 0.15) + (300000 * 0.20) + (total_income - 1500000) * 0.30

# print("Income tax payable is", income_tax)

        


