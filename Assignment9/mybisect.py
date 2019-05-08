f = lambda x: x**6 - x - 1

def sign(x):
    if x > 0:
        return 1
    else:
        return -1
# TO DO: Implement this function


def bisect(f,a,b,tau):
# TO DO: Implement this function
# Use the following print statement to display the data nicely
# the c variable is from the algorithmic specification of the bisection method seen above
# print("{0:.5f} {1:.5f} {2:.5f} {3:.5f} {4:.5f}".format(a,b,c,b-c,f(c)))
    c = (a + b)/2
    while (b - c) >= tau:
        print("{0:.5f} {1:.5f} {2:.5f} {3:.5f} {4:.5f}".format(a,b,c,b-c,f(c)))
        if (sign(b) * sign(c)) <= 0:
            a = c
        else:
            b = c
        c = (a + b)/2
    print("{0:.5f} {1:.5f} {2:.5f} {3:.5f} {4:.5f}".format(a,b,c,b-c,f(c)))

bisect(f,1.0,2.0,.001)