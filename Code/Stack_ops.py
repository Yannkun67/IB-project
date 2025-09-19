def stack_tracking():
    stack = []  
    stack = list()
    while True:
        for i in range(5):
            print("")
        try:
            print("------Select your options------")
            print(" 1. Push an item onto the stack")
            print(" 2. Pop an item from the stack")
            print(" 3. View the top item of the stack")
            print(" 4. Exit")
            print ("")
            choice = input("")

            if choice == "1":
                item = input("Enter the item to push onto the stack: ")
                stack.append(item)
                print(f"Pushed '{item}' onto the stack.")
            elif choice == "2":
                if len(stack) == 0:
                    print("Stack is empty, cannot pop.")
                else:
                    popped_item = stack.pop()
                    print(f"Popped '{popped_item}' from the stack.")
            elif choice == "3":
                if len(stack) == 0:
                    print("Stack is empty.")
                else:
                    top_item = stack[-1]
                    print(f"Top item is '{top_item}'.")
        except IndexError:
            print("Error wrong input, please try again")
            continue

    for i in range(5):    
       print("")


stack_tracking()