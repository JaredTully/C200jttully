#imports needed
import numpy as np
import math
import numpy as np
import matplotlib.pyplot as plt

#INPUT ax**2 + bx + c = 0 coefficients to quadratic
#RETURN tuple (x,y) that are solutions
def q(a,b,c):
    if (b**2 - 4 * a *c) == 0:
        x2 = (-1 * b)/(2 * a)
        x1 = (-1 * b)/(2 * a)
        x = complex(x1, x2)
        print("Not Complex")
        return (x.real, x.imag)
    elif (b**2 - 4 * a *c) < 0: #not really sure how mathematically how to handle the negative sqrt 
        x2 = (-1 * b + math.sqrt(b**2 - 4 * a *c * -1))/(2 * a)
        x1 = (-1 * b - math.sqrt(b**2 - 4 * a *c * -1))/(2 * a)
        x = complex(x1 * 1.0j, x2 * 1.0j)
        print("Complex")
        return (x.real, x.imag)
    else:
        x2 = (-1 * b + math.sqrt(b**2 - 4 * a *c))/(2 * a)
        x1 = (-1 * b - math.sqrt(b**2 - 4 * a *c))/(2 * a)
        x = complex(x1, x2)
        print("Not Complex")
        return (x.real, x.imag)
    

# Tests
print(q(1,3,-4))
print(q(2,-4,-3))
print(q(9,12,4))
print(q(3,4,2))


# Test & fun stuff!
#assigns the two values into x and y
#because this returns a tuple (firstvalue, secondvalue)
x1,y1 = q(1,-2,-4) # x**2 - 2*x - 4 = 0
print(x1,y1)
#creates an anonymous function
#this is the function described above
#You should be intrigued by this assignment
#What is it doing?
f = lambda x:x**2 - 2*x - 4
#the output should be zero
print(f(x1),f(y1))

# Plotting Porition
# evenly sampled time at 200ms intervals
x = np.arange(-4.0, 5.0, 0.2)
# Green dashes for line
plt.plot(x, x**2 - 2*x - 4, 'g--')
# Blue dashes for line
plt.plot(x,3*x**2 + 4*x + 2, 'b--')
# Draw horizontal line
plt.plot([-4,4],[0,0], color='k', linestyle='-', linewidth=2)
# Plot red dots as solution
plt.plot([x1,y1],[0,0],'ro')
plt.show()
