# Task 1: Finish the following four functions

import math

def maxThree(x, y, z):
    
    varMax = x

    if varMax < y:
        varMax = y 
    if varMax < z:
        varMax = z
    if varMax < x:
        varMax = x

    return varMax

print(maxThree(3, 1, 2))
print(maxThree(3, 1, 5))
print(maxThree(3, 7, 5))
	
def minThree(x, y, z):

    varMax = x

    if varMax > y:
        varMax = y 
    if varMax > z:
        varMax = z
    if varMax > x:
        varMax = x

    return varMax

print(minThree(1, 2, 3))
print(minThree(1, 3, 2))
print(minThree(3, 2, 1))

def maxTwoSum(tomato, potato, idaho):
	
    p1 = tomato + potato
    p2 = tomato + idaho
    p3 = potato + idaho

    varMax = p1

    if p1 > p2:
        varMax = p1
    elif p2 > p3:
        varMax = p2
    else:
        varMax = p3

    return varMax    
	

print(maxTwoSum(3,2,1))

def minTwoSum(x, y, z):
    
    p1 = x + y
    p2 = x + z
    p3 = y + z

    varMax = p1

    if p1 < p2:
        varMax = p1
    elif p2 < p3:
        varMax = p2
    else:
        varMax = p3

    return varMax  
	
print(minTwoSum(3,2,1))	

# Task 2: Writing more functions

def circleArea(diamater):
	
    radius = diamater /2

    return math.pi * (radius ** 2)
	
print(circleArea(3))
    
def areaDifference_rect(L1, W1, L2, W2):
	
    a1 = L1 * W1
    a2 = L2 * W2

    diff = a1 - a2

    if diff < 0:
        diff = diff * -1 
	
    return diff

print(areaDifference_rect(1, 1, 2, 2))
	
def areaDifference_circle(d1, d2):
	
    a1 = circleArea(d1)
    a2 = circleArea(d2)
	
    diff = a1 - a2

    if diff < 0:
        diff = diff * -1 
	
    return diff
	
print(areaDifference_circle(1, 2))