def palindrome_num():
    num = input("What is the number? ")
    length = len(num)
    letters = list(num)

    palindrome_check = True
    for letter in range(length // 2):
        if letters[letter] != letters[length - letter - 1]:
            palindrome_check = False
            break

    if palindrome_check:
        print("It's a palindrome!")
    else:
        print("Not a palindrome.")

palindrome_num()