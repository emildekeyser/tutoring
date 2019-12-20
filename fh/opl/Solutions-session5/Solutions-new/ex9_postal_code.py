def sum_of_digits(number):
    s = 0
    while number > 0:
        s += number % 10
        number //= 10
    return s


def check_digit_of(number):
    s = sum_of_digits(number)
    # The extra modulo 10 at the end is needed to convert a check digit of 10 to 0
    result = (10 - s % 10)%10
    return result


def code_of(digit):
    if digit==1: return ":::||"
    if digit==2: return "::|:|"
    if digit==3: return "::||:"
    if digit==4: return ":|::|"
    if digit==5: return ":|:|:"
    if digit==6: return ":||::"
    if digit==7: return "|:::|"
    if digit==8: return "|::|:"
    if digit==9: return "|:|::"
    if digit==0: return "||:::"


def reverse_of(number):
    s=0
    while number > 0:
        r=number % 10
        s = s * 10 + r
        # Floor division (//) and assingment (=)
        number //= 10
    return s


def postal_bar_code_of(number):
    # Reverse order of number so the last digit of the number can be split off which is an easy operation
    rnumber=reverse_of(number)
    result=""
    while rnumber > 0:
        # Get last digit of the rnumber
        digit = rnumber % 10

        result += code_of(digit)
        result += " "

        # Remove last digit of the rnumber
        rnumber //= 10
    result += code_of(check_digit_of(number))
    return result


def main():
    number = int(input("Enter a postal code : "))
    print("The corresponding barcode is %s" % postal_bar_code_of(number))


main()