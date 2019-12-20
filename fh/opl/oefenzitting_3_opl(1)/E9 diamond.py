height = int(input('Enter the height of the diamond: '))

while height > 0:
    mid_height = height // 2
    for i in range(0, mid_height):
        output = ''
        for x in range(0, mid_height - i):
            output += ' '
        for y in range(0, i * 2 + 1):
            output += '*'
        print(output)

    if height % 2 == 1:
        output = ''
        for i in range(0, height):
            output += '*'
        print(output)

    for i in range(0, mid_height):
        output = ''
        for x in range(0, i + 1):
            output += ' '
        for y in range(0, 2 * (mid_height - i) - 1):
            output += '*'
        print(output)

    print()

    height = int(input('Enter the height of the diamond: '))
