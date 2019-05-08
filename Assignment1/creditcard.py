# get library for log function
import math

# get user inputs
APR = float(input("What is your APR: %")) #test with 19%
C = float(input("What is the amount owed on the credit card: $")) #test with 1000
p = float(input("What it the monthly payment made: $")) #test with 25 
i = (APR/100)/12

#complete code here
n = (- math.log10((1 - (i * C ) / p ))) / (math.log10(i + 1))

print("You’ll make ", math.ceil(n), " payments.")