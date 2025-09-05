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

        misspelled_words = set()
        for word in words:
            if word not in dictionary:
               misspelled_words.add(word)

    print("Number of words checked:", wcount)
    print ("Number of misspelled words:", len(misspelled_words))



Spellcheck()