def temperature_tracker():
    loop = 0
    maxtemp = 0
    lowtemp = 100
    tempincrease = 0
    tot = 0
    prevtemp = 100
    #all the variables for the program
    temp = open("hk-temperatures-2024.txt", "r")
    line = temp.readline()
    line = line.strip()
    while line != "":
        line = temp.readline()
        line = line.strip() #reads the line from the file and removes extra stuff
        if line:
            line = float(line)
            if line > maxtemp: #checks if the temps are higher or lower than the current max/low temp
                maxtemp = line
            elif line < lowtemp:
                lowtemp = line
            tot = tot + line #adds the temperature to the total for the av
            if line > prevtemp:#checks if the temperature increased from the day befro
                tempincrease = tempincrease + 1
                prevtemp = line
            else:
                prevtemp = line

            loop = loop + 1
    avg = tot / loop #calculates the average temperature
    print("The average temperature is", avg)
    print("The highest temperature is", maxtemp)
    print("The lowest temperature is", lowtemp)
    print("The number of days the temperature increased is", tempincrease)

temperature_tracker()