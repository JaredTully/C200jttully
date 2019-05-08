#INPUT temperature in Fahrenheit T, wind speed in mph V
#RETURN wind chill temperature
def windChill(T,V):
    out = 35.74 + (0.6215 * T) - (35.75 * (V ** 0.16)) +  0.4275 * T * V ** 0.16
    return out

print(windChill(25,5)) #should be 18.85...