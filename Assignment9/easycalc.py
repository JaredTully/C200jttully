import math

# INPUT function fn, start is a, end is b,
# n is an even number of intervals
# RETURN approximate area under the curve
def simpson(fn,a,b,n):
    delta_x = (b - a)/n
    interval = lambda i: a + i*delta_x
    summ = 0
    #print(n)
    for x in range(0,n+1):
        if x == 0 or x == (n):
            summ += fn(interval(x))
            #print("if")
        elif x % 2 == 1:
            summ += (4 * fn(interval(x)))
            #print("elif1")
        elif x % 2 == 0:
            summ += (2 * fn(interval(x)))
            #print("elif2")
            
    return delta_x * summ * (1/3)

# convert string to either number or expression
def convert(x):
    if x.isnumeric():
        return float(x)
    else:
        return eval(x)

with open("integralfile.txt", "r") as xfile:
    xlines = [d.split(",") for d in xfile.read().split("\n")]

for i in xlines:
    body = i[0]
    fn = eval("lambda x : " + body)
    a = convert(i[1])
    b = convert(i[2])
    n = convert(i[3])
    answer = convert(i[4])
    integration = simpson(fn,a,b,n)
    error = abs((answer - integration)/answer)
    print("f(x) = {0} over [{1},{2}] is {3:.3f}".format(body,a,b,integration))
    print("Actual answer is {0:.3f}".format(answer))
    print("Error is {0:.3f}".format(error))
