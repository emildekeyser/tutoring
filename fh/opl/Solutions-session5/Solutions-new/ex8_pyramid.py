def pyramid1(height, symbol='#'):
    for i in range(height):
        # Instantly print out the sequence of symbols
        print(' '*(height-i-1) + symbol*(i*2+1))


def pyramid2(height, symbol='#'):
    ret = ''
    for i in range(height):
        # Concatenate the strings of symbols and split them with the newline character '\n'
        ret = ret + ' '*(height-i-1) + symbol*(i*2+1) + '\n'
    return ret


def main():
    height = int(input("enter height of pyramid: "))
    while height < 1 :
        height = int(input("enter positive integer: "))

    pyramid1(height)

    p = pyramid2(height, '*')
    print(p)


main()