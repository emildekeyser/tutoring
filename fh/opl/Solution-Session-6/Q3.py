import string
def clean_word(word):
    return word.lower().strip(string.punctuation)

def get_voc(text):
    voc = set()
    words = text.split()
    for word in words:
        cleaned_word = clean_word(word)
        if cleaned_word != "":
            voc.add(cleaned_word)
    return voc

voc = set()
txt = input("Input a text: ")
list_vocs = []  # to store all the voc of typed sentences

while txt != "QQQ":
    this_voc = get_voc(txt)
    list_vocs.append(this_voc)
    newvoc = voc.union(this_voc)
    print("New size of the vocabulary: ", len(newvoc))
    print("Words newly added: ", ", ".join(newvoc.difference(voc)))
    voc = newvoc
    txt = input("Input a text: ")

result = set()
for word in voc:
    count = 0  # variable to count the number of times w occur in one voc
    for ite_voc in list_vocs:
        if word in ite_voc:
            count += 1
    if count > len(list_vocs) // 2:
        result.add(word)

output_string = ""
for word in result:
    output_string += word
    output_string += " "

print("Words occurring in more than 50% of the input texts: " + output_string)
