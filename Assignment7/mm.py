b, r, y, g = "b", "r", "y", "g"

def result(hidden, guess):
    oh, og = hidden, guess
    dp, dcc = {}, {}
    for x in [b, r, y, g]:
        dp[x] = 0
        dcc[x] = 0
    
    for i in range(len(og)):
        if og[i] == oh[i]:
            dp[og[i]] += 1
    
    for i in range(len(og)):
        if og[i] in oh:
            dcc[og[i]] += 1

    print("LOC", end="")
    print(dp)
    print("COL", end="")
    print(dcc)
    print("{0:<4} is hidden pattern". format(oh))
    print("{0:<4} is your guess".format(og))