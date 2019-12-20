status = input("Please enter your marital status: ")
income = float(input("Please enter your annual income: "))
tax = 0

if "single" in status:
    if income > 8000:
        tax += 8000 * 0.1
        if income > 32000:
            tax += 26000 * 0.15
            tax += (income - 32000) * 0.25
        else:
            tax += (income-8000) * 0.15
    else:
        tax += income * 0.1

elif "married" in status:
    if income > 16000:
        tax += 16000 * 0.1
        if income > 64000:
            tax += 48000 * 0.15
            tax += (income - 64000) * 0.25
        else:
            tax += (income-16000) * 0.15
    else:
        tax += income * 0.1


print("On " + str(income) + " income and your marital status being " + status + " you have to pay " + str(tax) + " taxes.")


