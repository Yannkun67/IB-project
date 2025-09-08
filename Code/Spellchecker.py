def Spellcheck():
    import string
    import os
    base_path = os.path.dirname(__file__)
    text_path = os.path.join(base_path, "mystery-text.txt")
    dict_path = os.path.join(base_path, "dictionary.txt")

    with open(text_path, "r") as text, open(dict_path, "r") as dicti:
        dictionary = set(word.strip().lower() for word in dicti)
        words = []
        lines = 0
        wcount = 0
        misspelled = 0
        misspelled_words = set()
        for line in text: #loops through the file an puts it ito a list
            line = line.strip().lower()
            line = line.translate(str.maketrans('', '', string.punctuation)) #got chatgpt to help with this
            for word in line.split():
                words.append(word)
                wcount = wcount + 1

        
        for word in words:
            if word not in dictionary:
                misspelled = misspelled + 1
                misspelled_words.add(word)
    print("Number of words checked:", wcount)
    print ("Number of misspelled words:", len(misspelled_words))



Spellcheck()