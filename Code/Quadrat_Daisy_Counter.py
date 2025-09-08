def count_daisies():
    daisy_counter = []
    num = 1
    while True:
        for i in range(5):
            print("")
        print ("------Select your options------")
        print (" 1. Input  daisies per quadrat")
        print (" 2. View the last entry")
        print (" 3. Remove the last entry")
        print (" 4. Count total daisies")
        print ("")
        choice = input("")
        print("")


        try:
            if choice == "1":
                daisies = int(input("Enter the number of daisies in quadrant " + str(num) + ": "))
                daisy_counter.append(daisies)
                num = num +1
                print ("Saved", daisy_counter)
            elif choice == "2":
                print ("The last entry was: " + str(daisy_counter[-1]))

            elif choice == "3":
                if len(daisy_counter) == 0:
                    print ("There are no entries to remove")
                else:
                    removed = daisy_counter.pop()
                    num = num - 1
                    print ("Removed the last entry of: " + str(removed))

            elif choice == "4":
                total = sum(daisy_counter)
                print ("The total number of daisies counted is: " + str(total))
                break

            else:
                print("Invalid input, please try again")

            return
                 
        except ValueError:
            print("Invalid input, a number is required")
            continue
        

    for i in range(5):    
           print("")
        
count_daisies()