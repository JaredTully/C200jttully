def removecnt(xlst, x):
    
    tmpLst = []

    cnt = 0

    for i in xlst:
        if i != x:
            tmpLst += [i]
        else:
            cnt += 1

    xlst = tmpLst

    return(xlst, x, cnt)

def myMin(xlst):
    mini = xlst[0]
    for x in xlst:
        if x < mini:
            mini = x
    return mini

def insertionSort(xlst):
    rtnLst = []
    
    m = xlst[0]

    while xlst:
        toRemove = myMin(xlst)
        removed = removecnt(xlst, toRemove)
        xlst = removed[0]
        for x in range(removed[2]):
            rtnLst += [removed[1]]

    return rtnLst
