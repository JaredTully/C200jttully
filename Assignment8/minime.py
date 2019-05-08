def min(x,y):
    if x < y:
        return x
    else:
        return y

def MIN(lst):
    #print(lst)
    if len(lst) > 1:
        if lst[0] < lst[1]:
            lst.remove(lst[1])
            return MIN(lst)
        else:
            lst.remove(lst[0])
            return MIN(lst)
    else:
        return lst[0]
        

# for loop and index into list
def min1(x):
    mini = x[0]
    for i in range(len(x)):
        if x[i] < mini:
            mini = x[i]
    return mini 


# for loop and list iteration
def min2(x):
    mini = x[0]
    for i in x:
        if i < mini:
            mini = i
    return mini 


# while loop and index 
def min3(x):
    mini = x[0]
    count = 0 
    while count < len(x):
        if x[count] < mini:
            mini = x[count]
        count += 1
    return mini 

# while loop list iteration
def min4(x):
    mini = x[0]
    while x:
        if x[0] < mini:
            mini = x[0]
        x = x[1::]
    return mini 


def min5(x):
    small = x[-1]
    for i in range(len(x)-1,-1,-1):
        if x[i] < small:
            small = x[i]
    return small

x = [1,42,-1,22,0,12]


mf = [MIN, min1, min2, min3, min4, min5]

for f in mf:
    print("{0}({1}) = {2}".format(f.__name__,x,f(x)))