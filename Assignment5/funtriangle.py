for x in range(1, 11, 1):
    print("*"*x)
for x in range(1, 11, 1):
    print("*"*(10-x))


a = 0
for i in range(10):
    a += i
    print("*" * a)
    #print(a) 

a = 45
for i in range(9, 0, -1):
    a -= i
    print("*" * a)


for i in range(11):
    temp = (" " * i) + ("*" * (21 - (2*i))) + (" " * i)
    print(temp)