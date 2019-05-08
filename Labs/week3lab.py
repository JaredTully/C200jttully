def meaning(someString):
    if someString == ":)":
        rtn = 1
    elif someString == "-.-":
        rtn = 2
    elif someString == ":(":
        rtn = 3
    elif someString == ":O" or someString == ":0" or someString == ":o":
        rtn = 4
    elif someString == ":P" or someString == ":p":
        rtn = 5
    else:
        rtn = 0
    return rtn

print(meaning(":)"))
print(meaning("-.-"))
print(meaning(":("))
print(meaning(":O"))
print(meaning(":P"))
print(meaning(""))

def drinks(age, kidOverride):
    if (((age > 30 and age < 35) or age == 35) and kidOverride == 0):
        print("Cherry Coke")
    if (((age > 35 and age < 40) or age == 40) and kidOverride == 0):
        print("Coke")
    if ((age > 40 and age < 45) and kidOverride == 0):
        print("Diet Coke")
    elif ((age >= 45) and kidOverride == 0):
        print("Ice Tea")
    elif ((age <= 30) and kidOverride == 0):
        print("Pepsi")
    if (age > 30 and kidOverride == 1):
        print("Guess I am a kid and drinking Pepsi")
    if (age > 30 and kidOverride == 2):
        print("Orange soda is fun")
    if (age > 30 and kidOverride == 3):
        print("Dr. Pepper is best soda dont @ me")

drinks(25, 0)
drinks(30, 0)
drinks(32, 0)
drinks(35, 0)
drinks(37, 0)
drinks(40, 0)
drinks(42, 0)
drinks(45, 0)
drinks(47, 0)
drinks(35, 1)
