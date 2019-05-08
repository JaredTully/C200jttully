import matplotlib.pyplot as plt
import numpy as np

abscissa = np.arange(20)
plt.gca().set_prop_cycle('color', ['red', 'green', 'blue', 'black'])

class MyLine:

    def __init__(self, *args,**options):
        if len(args) == 2:
            if (type(args[0]) == tuple and type(args[1]) == tuple) or "2pts" in options.values():
                self.slope = (args[1][1]-args[0][1])/(args[1][0]-args[0][0])
                self.intercept = args[0][1] - self.slope * args[0][0]
                self.line = lambda x: self.slope * x + self.intercept
            elif "point-slope" in options.values():
                self.slope = args[1]
                self.intercept = args[0][1] - self.slope * args[0][0]
                self.line = lambda x: self.slope * x + self.intercept
        elif "lambda" in options.values():
            self.line = lambda x: eval(args[0])
            self.intercept = self.line(0)
            self.slope = self.line(1) - self.line(0)
            

    def draw(self):
        plt.plot(abscissa,self.line(abscissa))

    def get_line(self):
        return "y = {0:.2f}x + {1:.2f}".format(self.slope, self.intercept)

    def __str__(self):
        return self.get_line()

    def __mul__(self,other):
        if self.slope == other.slope:
            return ()
        else:
            m = self.slope + (-1 * other.slope)
            b = other.intercept - self.intercept
            x = b / m
            y = self.line(x)
            return (round(x,3),round(y,3))

x1 = MyLine((0,0), (5,5),options = "2pts")
x1.draw()
x2 = MyLine((5,0),-1/4, options = "point-slope")
x2.draw()
x3 = MyLine("(-4/5)*x + 5", options = "lambda")
x3.draw()
x4 = MyLine("x + 2", options = "lambda")
x4.draw()

print("The intersection of {0} and {1} is {2}".format(x1,x2,x1*x2))
print("The intersection of {0} and {1} is {2}".format(x1,x3,x1*x3))
print("The intersection of {0} and {1} is {2}".format(x1,x4,x1*x4))


plt.legend([x1.get_line(), x2.get_line(), x3.get_line(),x4.get_line()],loc='upper left')
plt.show()