#TIMER FUNCTION -- deprecated in 3.8 FYI
#so you might get messages -- you can ignore them for now
import time

def ftimer(f,args):
    time_start = time.clock()
    f(args)
    time_elapsed2 = (time.clock()-time_start)
    return time_elapsed2

#1
def even(x):
    if (x % 2) == 1:
        return False
    else:
        return True

#2
def odd(x):
    if (x % 2) == 0:
        return False
    else:
        return True

#3
#Recursive
#INPUT n
#OUTPUT RE value
def b(n):
    if n == 1 or n == 2:
        return 0
    elif even(n):
        return n - 1 + b(n-1)
    elif odd(n):
        return n**2 + 1 + b(n-1)

#4
#TAIL RECURSIVE FOR 3
def btr(n,s):
    if n == 1 or n == 2:
        return s
    elif even(n):
        return btr(n-1, s + (n-1))
    elif odd(n):
        return btr(n-1, s + (n**2 + 1))


#5 
#MEMOIZATION 
#USE THIS DICTIONARY
d = {2:0,1:0}
def bm(n):
    if n == 0:
        return 0
    elif even(n):
        if not n in d.keys():
            return bm(n-1) + n - 1 
        else:
            return bm(n-1) + d[n]
    elif odd(n):
        if not n in d.keys():
            return bm(n-1) + n**2 + 1
        else:
            return bm(n-1) + d[n] 
#6
# LINEARIZATION        
def bL(n):
    x,y=0,0
    for i in range(1,n+2):
        if i == n+1:
            return y
        elif i == 1 or i == 2:
            x,y=x,y
        elif even(i):
            x,y=y,y+(i-1)
        elif odd(i):
            x,y=y,y+(i**2+1)

for i in range(1,10): 
    print("f({0}) = {1}, {2}, {3}, {4}".format(i, b(i),btr(i,0),bm(i),bL(i) ))

fblist = [b, lambda i: btr(i,0), bm ,bL]
tlist = [round(ftimer(f,700)*10**5,2) for f in fblist]
print(tlist)
print()
###################################################

#7
#RECURSIVE IMPLMENTATION
#INPUT N
#OUTPUT RE VALUE
def gg(n):
    if n == 0:
        return 1
    else:
        return 1 + 2 * gg(n-1)

#8
#TAIL RECURSIVE
def gtr(n,s):
    if n == 0:
        return 1 + s
    else:
        return gtr(n-1, (s +1) * 2 )

#9
#MEMOIZATION DICTIONARY INSIDE
def gm(n):
    d = {}
    if n ==0:
        return 1
    else:
        if not n in d.keys():
            d[n] = 1 + 2 * 2
            return 1 + 2 * gm(n-1)
        else:
            return d(n) + gm(n-1)


#10
#LINEARIZATION
def gL(n):
    x,y = 0,0
    for i in range(1,n+2):
        if i == n+1:
            return y +1
        else:
            x,y=y,(2*(y+1))

fglist = [gg, lambda i: gtr(i,0),gm, gL]

for i in range(0,10):
    print("f({0}) = {1}, {2}, {3}, {4}".format(i,gg(i),gtr(i,0),gm(i),gL(i)))

tlist = [round(ftimer(f,700)*10**5,2) for f in fglist]
print(tlist)

