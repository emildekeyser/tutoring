hex_dict = {}

for num in range(1, 10):
    hex_dict[str(num)] = num

#ord returns the unicode code for the given character
#chr converts a unicode code to the corresponding character
#iterating from ord('A') to ord('F') + 1 will iterate over all unicode codes for the characters 'A','B','C',...,'F'
for num in range(ord('A'), ord('F') + 1):
    hex_dict[chr(num)] = 10 + num - ord('A')
    hex_dict[chr(num).lower()] = 10 + num - ord('A')

def convert(hex_num):
    val = 0

    for i in range(len(hex_num) - 1, -1, -1):
        val += hex_dict[hex_num[i]] * (16 ** (len(hex_num) - 1 - i))

    # OR:
    # for c in hex_num:
    #     val = 16 * val + hex_dict[c]

    return val

hex_num = input("Input a hex number: ")
print(convert(hex_num))
