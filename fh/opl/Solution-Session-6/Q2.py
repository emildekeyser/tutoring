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

txt = input("Input a text: ")
print(get_voc(txt))
