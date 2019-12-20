'''
keys = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
'''
keys = {}
for i in range(ord('A'), ord('Z') + 1):
    if i + 13 <= ord('Z'):
        keys[chr(i)] = chr(i + 13)
        keys[chr(i).lower()] = chr(i + 13).lower()
    else:
        keys[chr(i)] = chr(i - 13)
        keys[chr(i).lower()] = chr(i - 13).lower()

print(keys)



def rot13(s):
    result = ""
    for c in s:
        if c in keys.keys():
            result += keys.get(c)
        else:
            result += c

    return result

print(rot13("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"))
print(rot13("Caesar cipher?  I much prefer Caesar salad!"))
