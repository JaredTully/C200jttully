import numpy as np 

x = np.arange(0.00, 1, .01)

y = []

for i in x:
    i = i * 100
    i = round(i)

    if (i % 2) != 0:
        i = i / 100
        y += [i]

#really loved that the printing to only 14 lines at a time was way harder than the actual math xD
#but I know that I definitetly did the printing harder than it had to be 
#but I had fun playing with loops 

output = ""
incr = 0
for i in y:
    if incr == 0:
        output = str(i)
        incr += 1
    elif incr < 14:
        output = output + " " + str(i)
        incr += 1
    else:
        print(output)
        output = str(i)
        incr = 1

out2 = ""

for i in y:
    if i == 0.85:
        out2 = str(i)
    elif i > 0.85:
        out2 = out2 + " " + str(i)

print(out2)