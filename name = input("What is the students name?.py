fname = ""
mname = ""
lname = ""
def mnamerepeat():
    loop1 = 0
    while loop1 == 0:
        mname = input("What is the students middle name?")
        yorn = input("Does the student have another middle name?")
        if yorn == "No" or "no":
            loop1 = 1
        elif yorn == "Yes" or "yes":
            return

fname = input("What is the students first name?")
mnamerepeat()
lname = input("What is the students last name?")
fname3char = fname[0:3]#used outside help
print(fname3char)
