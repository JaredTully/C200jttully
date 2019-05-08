#INPUT list of jellybeans [y,r,g,...]
#RETURN tuple (gsum, rsum, ysum, total)
# gsum is total green, rsum is total red
# ysum is total yellow and total = beans
def CountBeans(xlst):
    gsum = 0
    rsum = 0
    ysum = 0
    for i in xlst:
        if i == "y":
            ysum += 1
        elif i == "g":
            gsum += 1
        elif i == "r":
            rsum += 1

    total = gsum + rsum + ysum
    return (gsum, rsum, ysum, total)

y,g,r = "y","g","r"

beans = [y,y,g,g,y,y,y,g,g,g,g,y,y,y,y,y,y,y,r,r,r,r,r,r,r,r,r,r,y,y,r,g,g,y,r,r,r,y,y,y,g,r]

print("g={0}, r={1}, y={2}, total={3}".format(*CountBeans(beans)))