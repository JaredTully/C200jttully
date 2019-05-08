#imports
import math 

######################################
#
# DATA 
#
#All values $/ounce abbreviated $/Oz
Gold = 1333.20 #up 2.00
Silver = 16.10 #no change
Platinum = 825.15 #up 4.25
Palladium = 1344.90 #down 22.80

Au, Ag, Pl, Pa = "Au", "Ag", "Pl", "Pa" # to make use of symbols easier

account = 100000  # $100,000 cash assets
#
#######################################
#INPUT metal and amount in ounces you want to purchase
#RETURN the cost of the amount of metal you're purchasing
def preciousMetalToDollars(metal, amt):
    if metal == "Au":
        return (amt * Gold)
    elif metal == "Ag":
        return (amt * Silver)
    elif metal == "Pl":
        return (amt * Platinum)
    elif metal == "Pa":
        return (amt * Palladium)

#INPUT The dollar amount you want to spend on a metal
#RETURN The maximal ounces you can purchase and what's left in your account
#I am including two statements that you'll need that I will explain on Monday
#I am also leaving in the print statements -- which might be decent hints
#Presuming there's not another vortex
def dollarsToMetals(amt, metal):
    global account
    amtCanBuy = int(amt / preciousMetalToDollars(metal, 1))
    oneOunce = preciousMetalToDollars(metal, 1)
    totalCost = amtCanBuy * preciousMetalToDollars(metal, 1)
    account = account - totalCost
    #TO DO: IMPLEMENT FUNCTION

    print("\n{0} @ ${1:.2f} can buy {2} Oz costing${3:.2f}".format(metal,oneOunce,amtCanBuy,totalCost))
    print("You currently have ${0:.2f} in your account.".format(account))
   

print("Amt {0} is ${1:.2f}".format(Au,preciousMetalToDollars(Au,5)))
print("Amt {0} is ${1:.2f}".format(Ag,preciousMetalToDollars(Ag,4)))
print("Amt {0} is ${1:.2f}".format(Pl,preciousMetalToDollars(Pl,3)))
print("Amt {0} is ${1:.2f}.".format(Pa,preciousMetalToDollars(Pa,2)))        

dollarsToMetals(Gold,Au)
dollarsToMetals(25554,Pa)
dollarsToMetals(1000,Ag)
