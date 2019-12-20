def pascal(col, row):
    if row == 0 or col == 0 or row == col:
        return 1
    else:
        return pascal(col, row - 1) + pascal(col - 1, row - 1)


def main():
    for i in range(0, 10):
        for j in range(0, i + 1):
            print(pascal(j, i), end = " ")
        print("")

main()
