letter_height_inches = 8.5
letter_width_inches = 11
millimeter_per_inch = 25.4

# convert the inches to millimeters
letter_height_mms = letter_height_inches * millimeter_per_inch
# round the number down to one decimal place, remove the line below to see what happens otherwise
letter_height_mms = round(letter_height_mms, 1)

letter_width_mms = letter_width_inches * millimeter_per_inch
letter_width_mms = round(letter_width_mms, 1)

# convert the numbers to strings so when can concatenate them
print("USA letter dimension in millimeters: " + str(letter_height_mms) + " x " + str(letter_width_mms))
