first = int(input("first number? "))
second = int(input("second number? "))
third = int(input("third number? "))

common_begin = "The inputs in sorted order are: "

if first < second:
    if second < third:
        print(common_begin + str(first) + ", " + str(second) + " and " + str(third))
    elif third < first:
        print(common_begin + str(third) + ", " + str(first) + " and " + str(second))
    else:
        print(common_begin + str(first) + ", " + str(third) + " and " + str(second))
else:
    if first < third:
        print(common_begin + str(second) + ", " + str(first) + " and " + str(third))
    elif third < second:
        print(common_begin + str(third) + ", " + str(second) + " and " + str(first))
    else:
        print(common_begin + str(second) + ", " + str(third) + " and " + str(first))



