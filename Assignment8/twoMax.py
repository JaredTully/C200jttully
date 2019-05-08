import random as rn 

def twoMax(xlist):
    def twomax(x,y):
        return x * (x>y) + y * (x<=y)

    if xlist:
        return [twomax(xlist[0][0], xlist[0][1])] + twoMax(xlist[1::])

    else:
        return []

testlst = rn.randint(0,10)
lst = []
while testlst:
    lst.append([rn.randint(0,20),rn.randint(0,20)])
    testlst -= 1

print(lst)
answer = twoMax(lst)
print(answer)