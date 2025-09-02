def Spellcheck():
    import string
    with open("mystery-text.txt", "r") as text, open("dictionary.txt", "r") as dicti:
        dictionary = set(word.strip().lower() for word in dicti)
        words = []
        lines = 0
        wcount = 0
        misspelled = 0
        for line in text: #loops through the file an puts it ito a list
            line = line.strip().lower()
            line = line.translate(str.maketrans('', '', string.punctuation)) #got chatgpt to help with this
        for word in line.split():
            words.append(word)
            wcount = wcount + 1
        for word in words:
            if word not in dictionary:
                print(word, "is misspelled")
                misspelled = misspelled + 1
    print("Number of words checked:", wcount)
    print ("Number of misspelled words:", misspelled)



Spellcheck()