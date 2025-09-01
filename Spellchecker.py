def Spellcheck():
    import string
    text = open("mystery-text.txt", "r")
    dicti = open("dictionary.txt", "r")
    dline = dicti.readline()
    words = []
    lines = 0
    wcount = 0
    for line in text: #loops through the file an puts it ito a list
        line = line.strip()
        line = line.lower()
        line = line.translate(str.maketrans('', '', string.punctuation)) #got chatgpt to help with this
        for word in line.split():
            words.append(word)
            wcount = wcount + 1
    print (wcount)
Spellcheck()