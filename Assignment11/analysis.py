def insertionSort(xlst):
    rtnLst = []

    while xlst:
        maxx = max(xlst)

        for i in range(xlst.count(maxx)):
            rtnLst.append(maxx)
            xlst.remove(maxx)

    return rtnLst


usLst = []

with open('./Assignment11/foo.csv') as file:
    lines = list(file.readlines()) #making list where every entry is a string of the csv entry

usLst = []

for x in range(len(lines)) :
    a = lines[x].split(",")
    if a[3] == "US":
        temp = ()
        for y in range(len(a)):
            if y != len(a) -1:
                temp += (a[y],)
            else:
                temp += (a[y].replace("\n",""),)

        usLst += [temp]

fullList = []
popLst = []

for x in usLst:
    popLst += [int(x[4])]
    fullList.append((int(x[4]),x[0]))

sortedPop = insertionSort(popLst)

cityLst = []

rtnLst = []

for x in sortedPop:
    for i in range(len(fullList)):
        if x == fullList[i][0] and fullList[i] not in rtnLst:
            cityLst.append(fullList[i][1])
            rtnLst.append(fullList[i])

#print(rtnLst)

with open('./Assignment11/mypop.txt', "w") as workFile:
    for x in rtnLst:
        workFile.write(str(x[0]) + " " + str(x[1] + "\n"))