import numpy as np

#INPUT two matrices a,b
#RETURN product ab
def mm(a,b):
    rtn = np.zeros((len(a),len(a)), dtype=int)
    for i in range(len(a)):
        for x in range(len(b[0])):
            for y in range(len(a[0])):
                rtn[i][x] += a[i][y] * b[y][x]
    return rtn


#INPUT scalar n and matrix a
#RETURN scalar product na
def sm(n,a):
    rtn = np.zeros((len(a),len(a[0])))
    for x in range(len(a)):
        for y in range(len(a[0])):
            rtn[x][y] += n * a[x][y]
    return rtn

#INPUT matrix n x m
#RETURN transpose matrix m x n
def tp(a):
    rtn = np.zeros((len(a[0]),len(a)))
    for x in range(len(a[0])):
        for y in range(len(a)):
            rtn[x][y] += a[y][x]
    return rtn


#INPUT two matrices a,b
#RETURN sum a + b
def add_m(a,b):
    rtn = np.zeros((len(a),len(a[0])))
    for x in range(len(a)):
        for y in range(len(a[0])):
            rtn[x][y] += a[x][y] + b[x][y]
    return rtn


a = np.array([[1,2,4],[3,4,3]])
b = np.array([[-1,0],[1,-5],[-3,1]])
print("numpy product\n", np.dot(a,b))
d = mm(a,b)
print(d)

print("numpy scalar product\n", 4*a)
e = sm(4,a)
print(e)

print("numpy tranpose\n", np.transpose(a))
f = tp(a)
print(f)

print("numpy addition\n", a + a)
g = add_m(a,a)
print(g)