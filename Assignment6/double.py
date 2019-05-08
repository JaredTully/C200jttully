import copy
#INPUT list
#RETURN each element is doubled
#USE FOR iterate over list
def d1(x):
    tmp = []
    for i in x:
        tmp += [i, i]
    return tmp

#INPUT list
#RETURN each element is doubled
#USE FOR use range
def d2(x):
    tmp = []
    for i in range(len(x)):
        tmp += [x[i], x[i]]
    return tmp

#INPUT list
#RETURN each element is doubled
#USE WHILE iterate over list using index
def w1(x):
    tmp = []
    i = 0
    while (i < len(x)):
        tmp += [x[i], x[i]]
        i += 1
    return tmp

#INPUT list
#RETURN each element is doubled
#USE WHILE iterate over list
def w2(x):
    tmp = []
    lst = x.copy()
    while lst:
        tmp += [lst[0], lst[0]]
        lst = lst[1::]
    return tmp