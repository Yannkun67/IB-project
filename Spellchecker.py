import string
text = open("mystery-text.txt", "r")
dict = open("dictionary.txt", "r")
dline = dict.readline()
loop = 0
word = text.readline()
word = word.strip()
word = word.lower()
word = word.translate(str.maketrans('', '', string.punctuation))

