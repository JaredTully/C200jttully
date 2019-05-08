def unmarriedTax(income):
#TO DO: IMPLEMENT FUNCTION

    if income >= 0 and income < 9700:
        tax = 0.1
    elif income >= 9700 and income < 39475:
        tax = 0.12
    elif income >= 39475 and income < 84200:
        tax = 0.22
    elif income >= 84200 and income < 160725:
        tax = 0.24
    elif income >= 160725 and income < 204100:
        tax = 0.32
    elif income >= 204100 and income < 510300:
        tax = 0.35
    else:
        tax = .37
    
    return( tax * income )

# 2 Finish this function
# Calculates the taxes a married person owes for 2018
# Input Parameters: amount of income in USD income
# Return Value: amount taxes owed (USD)
def marriedTax(income):
#TO DO: IMPLMEMENT FUNCTION

    if income >= 0 and income < 13850:
        tax = 0.1
    elif income >= 13850 and income < 52850:
        tax = 0.12
    elif income >= 52850 and income < 84200:
        tax = 0.22
    elif income >= 84200 and income < 160700:
        tax = 0.24
    elif income >= 160700 and income < 204100:
        tax = 0.32
    elif income >= 204100 and income < 510300:
        tax = 0.35
    else:
        tax = .37
    
    return( tax * income )

# Calculates the taxes an individual owes for 2018
# Input Parameters: amount of income in USD income and marital status Boolean maritalStatus
# Return Value: amount taxes owed (USD)
def tax(income, maritalStatus):
	if(maritalStatus):
		return marriedTax(income)
	else:
		return unmarriedTax(income)
		
############################
#   DATA
############################
UrsalaIncome,UrsalaMarried = 160726, True
KaiserIncome, KaiserMarried = 501000, True
ShilahIncome, ShilahMarried = 20, True

############################
#   TESTS
############################
print("Ursala owes ", tax(UrsalaIncome, UrsalaMarried))
print("Kaiser owes ", tax(KaiserIncome, KaiserMarried))
print("Shilah owes ", tax(ShilahIncome, ShilahMarried))

print()
############################
#   DATA
############################
UrsalaIncome,UrsalaMarried = 204099, False
KaiserIncome, KaiserMarried = 510310, False
ShilahIncome, ShilahMarried = 9400, False

############################
#   TESTS
############################
print("Ursala owes ", tax(UrsalaIncome, UrsalaMarried))
print("Kaiser owes ", tax(KaiserIncome, KaiserMarried))
print("Shilah owes ", tax(ShilahIncome, ShilahMarried))
