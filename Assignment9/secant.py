f = lambda x: x**6 - x - 1

def secant(f,x0,x1,tau):
# TO DO: Implement function
# Use the following print statement to display the data nicely
# print("{0:.5f} {1:.5f} {2:.5f} {3:.5f}".format(x0,f(x0),f(x1),x0-x1))
    x = 0
    #while x < 6:
    while abs(x1-x0) > tau:
        print("{0:.5f} {1:.5f} {2:.5f} {3:.5f}".format(x0,f(x0),f(x1),x0-x1))
        temp = x1
        x1 = x1 - f(x1) * ((x1 - x0)/(f(x1) - f(x0)))
        x0 = temp
        x += 1
        

secant(f,2.0,1.0,.0001)