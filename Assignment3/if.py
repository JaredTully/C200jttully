x = False
y = True
z = 12
a = 10
b = not (x or not (x or y)) and True

#1#################
if not b:
    print("Happy")
elif b and not x:
    print("Valentines")
else:
    print("day!")
###################


#2#################
if (z > a) or (2*a > z):
    print("C200")
if not ((z > a) or (2*a > z)):
    print("is bliss")
###################


#3#################
if ((x and y) or x):
    print(a)
###################


#4#################
if (2 > z) or not x:
    print("1")
if 2 == 1:
    print("2")
if not y and x:
    print("3")
if x:
    print("4")
###################

#5########################
def f(x):
    ##return (x==4)*100 + (x==3)*10 + (x==2)*1000 + (x!=4)*(x!=3)*(x!=2)*100000

    if (x == 4):
        return 100
    elif (x == 3):
        return 10
    elif (x == 2):
        return 1000
    else:
        return 100000

print(f(4))
print(f(3))
print(f(2))
print(f(1))
##########################