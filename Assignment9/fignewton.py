f = lambda x: x**6 - x - 1
fp = lambda x: 6*(x**5) - 1

def fpa(f):
    h = .000001
    return lambda x: (f(x+h)-f(x-h))/(2*h)

def newton(f,fp,x,tau):
    def n(x,i):
        while f(x) > tau:
            print("{0} {1:.5f} {2:.5f}".format(i,x,f(x)))
            x = x - f(x)/fp(x)
            i += 1
        return x
    n(x,0)

#newton(f,fp,1.5,.0001)
#newton(f,fpa(f),1.5,.0001)

def userNewton():
    
    f = str(input("Function: "))
    tau = float(input("tau: "))
    x0 = float(input("x0: "))
    interactions = float(input("Interactions: "))

    def newton2(f,tau,x0,interactions):
        h = .000001
        f_func = eval("lambda x: " + str(f))
        
        i = 0

        while f_func(x0) > tau and i < interactions:
            print("{0} {1:.5f} {2:.5f}".format(i,x0,f_func(x0)))
            fPrime = (f_func(x0 + h) - f_func(x0 -h)) / (2 * h)
            x0 = x0 - f_func(x0) / fPrime
            i += 1
            if i == interactions:
                print("number of iterations exceeded...")

    newton2(f,tau,x0,interactions)

userNewton()