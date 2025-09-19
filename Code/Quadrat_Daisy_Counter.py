def count_daisies():
    daisy_counter = []
    num = 1
    while True:
        for i in range(5):
            print("")
        print ("------Select your options------") #UI to make it look nice and to selct options
        print (" 1. Input  daisies per quadrat")
        print (" 2. View the last entry")
        print (" 3. Remove the last entry")
        print (" 4. Count total daisies")
        print ("")
        choice = input("") #User chooses options
        print("")


        try: #so that it works if user inputs wrong stuff
            if choice == "1": #if they put 1 they input amount of daisies
            
                daisies = int(input("Enter the number of daisies in quadrant " + str(num) + ": "))
                daisy_counter.append(daisies)
                num = num +1
                print ("Saved", daisy_counter)
                

            elif choice == "2": #if they put 2 they see last entry
                print ("The last entry was: " + str(daisy_counter[-1]))

            elif choice == "3":#if they put 3 they remove last entry
                if len(daisy_counter) == 0: #checks if there are entries to remove
                    print ("There are no entries to remove")
                else:
                    removed = daisy_counter.pop()
                    num = num - 1
                    print ("Removed the last entry of: " + str(removed))

            elif choice == "4":#if they put 4 they see total amount of daisies
                total = sum(daisy_counter)
                print ("The total number of daisies counted is: " + str(total))
                break

            else:
                print("Invalid input, please try again")

            
                 
        except ValueError: #if they put in something that isnt a number
            print("Invalid input, a number is required")
            continue
        

    for i in range(5):    
           print("")
        
count_daisies()