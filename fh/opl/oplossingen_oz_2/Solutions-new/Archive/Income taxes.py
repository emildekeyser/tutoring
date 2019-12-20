#remaining_income is the income for which tax still has to calculated
remaining_income = float(input("income"))
tax = 0
if remaining_income>500000:
    #if the remaining_income is higher than 500000 calculate tax for the part over 500000
    tax+=(remaining_income-500000)*0.6
        #the income for which tax still has to be calculated is now 500000 (because we already calculated tax for everything over 500000)
    remaining_income = 500000

if remaining_income>250000:
    #if the remaining_income is higher than 250000 calculate tax for the part over 250000
    tax += (remaining_income-250000)*0.5
        #the income for which tax still has to be calculated is now 250000 (because we already calculated tax for everything over 250000)
    remaining_income = 250000

if remaining_income>100000:
    #etc...
    tax += (remaining_income - 100000)*0.04
    remaining_income = 100000

if remaining_income>75000:
    tax += (remaining_income - 75000)*0.03
    remaining_income = 75000

if remaining_income>50000:
    tax += (remaining_income -50000)*0.02
    remaining_income = 50000

#now remaining_income will be =< 50000
tax += remaining_income*0.01

print("total tax "+str(tax))
