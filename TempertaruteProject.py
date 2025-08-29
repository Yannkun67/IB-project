loop = 0
maxtemp = 0
lowtemp = 100
tempincrease = 100
tot = 0
prevtemp = 100
temp = float(0)
temp = open("hk-temperatures-2024.txt", "r")
line = temp.readline()
line = line.strip()
line = temp.readline()
while line != "":
    line = temp.readline()
    line = line.strip()
    if line:
        line = float(line)
        if line > maxtemp:
            maxtemp = line
        elif line < lowtemp:
            lowtemp = line
        tot = tot + line
        if line > prevtemp:
            tempincrease = tempincrease + 1
        else:
            prevtemp = line

        loop = loop + 1
avg = tot / loop

print("The average temperature is", avg)
print("The highest temperature is", maxtemp)
print("The lowest temperature is", lowtemp)
print("The number of days the temperature increased is", tempincrease)
