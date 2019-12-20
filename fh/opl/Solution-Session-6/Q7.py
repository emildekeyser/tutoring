import string
import operator

def clean_word(word):
    return word.lower().strip(string.punctuation)

voc = {}
txt = input("Input a text: ")
while txt != "QQQ":
    temps = txt.split()
    for tmp in temps:
        tmp = clean_word(tmp)
        if tmp in voc.keys():
            voc[tmp] = voc[tmp] + 1
        else:
            voc[tmp] = 1
    txt = input("Input a text: ")


for word in voc.keys():
    print(word + "\t" + str(voc[word]))


sorted_words = sorted(voc.items(), key=operator.itemgetter(1), reverse=True)

num = int(input("N: "))
print(num, "most common words: ")
for i in range(num):
    if i < len(sorted_words):
        print(sorted_words[i][0], "\t", sorted_words[i][1])
