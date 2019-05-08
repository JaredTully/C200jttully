import astronomy as astr 

def F(m):
    def lbToKg(pnds):
        convt = pnds / 2.204622
        return convt 
    myWeight = lbToKg(m)
    
    newtons = (astr.gravitationalConstant * astr.earthMass * myWeight) / ((astr.earthDiameter /2 ) **2)

    return newtons

print("{0:.2f} Newtons.".format(F(143.3)))