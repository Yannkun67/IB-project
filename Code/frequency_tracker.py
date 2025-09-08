import string
def frequency_counter():
    text = []
    freq_counter = []
    unique_words = [] 
    loop = 0
    count = 0


    with open("frequency-counter.txt", "r", encoding="utf-8-sig") as freq: #this block reads the file and puts it inbto the text list
        for line in freq:
            line = line.strip().lower() #makes the words lowercase and removes punctuation
            line = line.translate(str.maketrans('', '', string.punctuation))
            words = line.split() #splits the line into words
            for word in words:
                text.append(word)
        #print(text)
    

        unique_words.append(text[0]) #adds the first word to the unique words list
        for word in text:
            if word not in unique_words:
                unique_words.append(word) #puts the word in the unique words list if it is not already there
        #print(unique_words) #prints the unique words list 
    
        #attempt to count the frequency of each word but used a list
        # for word in unique_words:
        #     while loop < len(text):
        #         if text[loop] == word:
        #             count = count + 1
        #             freq_count = str(unique_words) + " apears " + str(count) + " times"
        #             freq_counter[loop] = freq_count
        #         else:
        #             loop = loop + 1
        # print(freq_counter)


        freq_count = {} #found help online for making dictionaries and how to use them need to learn more though because i dont fully understand
        for word in text:
            if word in freq_count:
                freq_count[word] = freq_count[word] + 1
            else:
                freq_count[word] = 1
        # for word, count in freq_count.items():
        #     print(f"{word} appears {count} times")
        # print(freq_count) 

        items = list(freq_count.items())
        itemcount = len(items)
        for num_pass in range(itemcount):
            for index in range(0, itemcount - num_pass - 1):
                if items[index][1] < items[index + 1][1]:
                    temp = items[index]
                    items[index] = items[index + 1]
                    items[index + 1] = temp
        for word, count in items:
            print(f"{word} appears {count} times")
        
        # for word in freq_count:
        #     if freq_count[word] < freq_count[word + 1]:
        #         temp = freq_count[word]
        #         freq_count[word] = freq_count[word + 1]
        #         freq_count[word + 1] = temp
        # print(freq_count)

frequency_counter()