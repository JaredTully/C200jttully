def circuit(A, B, C):
    def Z(a, b, c):
        return( (a and b) or c)
    return((not Z(A, B, C)) or not C)

print(0,0,0,circuit(0,0,0))
print(0,0,1,circuit(0,0,1))
print(0,1,0,circuit(0,1,0))
print(0,1,1,circuit(0,1,1))
print(1,0,0,circuit(1,0,0))
print(1,0,1,circuit(1,0,1))
print(1,1,0,circuit(1,1,0))
print(1,1,1,circuit(1,1,1))