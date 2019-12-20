def balance(string, open = 0):
    if len(string) == 0:
        #This returns a condition that results in True/False
        return open == 0
    elif open < 0:
        return False

    if string[0] == "(":
        open += 1
    elif string[0] == ")":
        open -= 1

    return balance(string[1:], open)

def main():
    str = input("Enter a string: ")
    print(balance(str))

main()
