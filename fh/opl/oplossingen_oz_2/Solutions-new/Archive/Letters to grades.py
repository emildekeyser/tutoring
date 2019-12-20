input_string = input("Enter a letter grade: ")


increment = input_string.find("+") > 0
decrement = input_string.find("-") > 0

value = 0
if input_string.startswith("D"):
    value = 1
elif input_string.startswith("C"):
    value = 2
elif input_string.startswith("B"):
    value = 3
elif input_string.startswith("A"):
    value = 4
#The following if statements checks whether the user input doesn't contain an increment AND a decrement and the grade F doesn't increment or decrement
if not (increment and decrement) and not ((increment or decrement) and value == 0):
    if increment:
        value += 0.3
    if decrement:
        value -= 0.3
    #The following if statments insures that the grade never goes above 4
    if value > 4.0:
        value = 4.0
    print("Numeric value: ", value)
else:
    print("Invalid input")
