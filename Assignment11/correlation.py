import matplotlib.pyplot as plt
import numpy as np
import math

def mean(lst):
    return (sum(lst) / len(lst))

def s(lst,setMean):
    temp = 0
    for x in lst:
        temp += (x-setMean)**2
    return math.sqrt( (1/(len(lst)-1)) * temp )

def sd(xlst):
    x,y = [],[]
    for i in range(len(xlst)):
        x += [xlst[i][0]]
        y += [xlst[i][1]]
    
    meanX = mean(x)
    meanY = mean(y)

    sX = s(x,meanX)
    sY = s(y,meanY)

    summ = 0 

    for a,b in zip(x,y):
        summ += ((a - meanX)/sX) * ((b - meanY)/sY)

    return 1/(len(x)-1) * summ

x = [[2,3],[4,3],[1,1.4],[1,.5],[5,3]]

#TO DO: Complete code
r = sd(x)

print(r)
plt.plot([i[0] for i in x],[i[1] for i in x], 'ro')
t = np.arange(0,6,.1)
plt.plot(t,t*.65 + .5,'g--')
plt.axis([0,6,0,6])
plt.xlabel("A values")
plt.ylabel("B value")
plt.title("r = {0:.3}".format(r))
plt.savefig("./Assignment11/stock.png")
plt.show()