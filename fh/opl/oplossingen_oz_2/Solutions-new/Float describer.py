number = float(input("Input a floating-point number: "))

if number == 0:
    print("The number is zero.")
elif number > 0:
    sign = "positive"
else:
    sign = "negative"


if abs(number) < 1:
    size = "small"
elif abs(number) > 1000000:
    size = "large"
#NOTE, the last else is necessary otherwise the variable size can be undefined
else:
    size = ""

#NOTE You need to check again that the value isn't equal to 0, if the value is equal to zero the variables SIZE and SIGN won't have a value (undefined)
if number != 0:
    print("This number is a " + size + " " + sign + " number.")








