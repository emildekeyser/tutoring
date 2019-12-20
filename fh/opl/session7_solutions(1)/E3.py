#E3 a
def reverse(string):
    if string == "":
        return ""
    #recall using index -1 takes the last element of a list (a string is also a list of charachters)
    return string[-1] + reverse(string[0:-1])

# E3 b
def substring(sub, string):
    if len(string) < len(sub):
        return False
    if string[0:len(sub)].lower() == sub.lower():
        return True
    else:
        return substring(sub, string[1:])

# E3 c
def index(sub, string, position = 0):
    if len(string) < len(sub):
        return -1
    if string[:len(sub)].lower() == sub.lower():
        return position
    else:
        return index(sub, string[1:], position + 1)
