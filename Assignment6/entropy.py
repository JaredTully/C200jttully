import math
#INPUT list of immutable objects
#RETURN list of probabilities
def makeProbability(xlst):
    tmp = []
    d = {}
    for x in xlst:
        if not x in d.keys():
            count = 0
            for i in xlst:
                if i == x:
                    count += 1
            d[x] = count / (len(xlst))
    for val in d.values():
        tmp += [val]

    return tmp

def entropy(xlst):
    sum = 0
    
    for x in xlst:
        if x != 0:
            sum += -1 * ( x * math.log2(x) )
        else:
            pass 
    return round(sum,2)

