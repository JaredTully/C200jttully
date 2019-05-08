def budgetSummary(categoryFileLocation, expenseFileLocation):
    """
    Given the file locations for category and expense, call the method
    readCategory(categoryFileLocation)
    and 
    readExpenses(expenseFileLocation)
    From here:
    Imagine that you wish to track your monthly expenses by category.  For example, housing might include rent, and the various utilities.  You have categorized all of the important expenses in a dictionary of the form 
    {expense : category, ...}. Each month your bank gives you a list of all your expenses in the form of [ (expense, amount),...], where expense could appear more than once in the list. 
    Write a function that returns a dictionary of the form { category : total, ... }. Have a special category `miscellaneous' for any expense that does not appear in your mapping.  
    Do not include categories for which there are no corresponding expenses
    """

    categoryDict = readCategory(categoryFileLocation)
    expenseList = readExpenses(expenseFileLocation)
    expenses = {}

    # TODO: Complete based off the comment description

    return 

def readCategory(location):
    """
    Reading the file from the location, where the first column is the 
    *expense*, the other column is the *category*, which is separated by " ABC ".
    Hint: Use split method on a string (look at python documentation)
    """
    result = {}

    with open(location, "r") as fle:
        for line in fle:
            splt = line.split(" ABC ")
            result[splt[1]] = splt[0]

    return result

def readExpenses(location):
    """
    Reading the file from the location, where the first column is 
    the *expense*, second column is the *amount*, separated by a ",".
    Return a list of tuples while reading the file.  
    """
    result = []

    with open(location, "r") as fle:
        for line in fle:
            splt = line.split(",")
            result += (splt[0], splt[1])

    return result

def drawTriangle1(location):
    """
    From the triangle question in an old homework, 
    generated triangle 1. 
    Given a location, write to a file the result of triangle one
    
    Return what contents were written to the file. 
    """

    finalResult = ""

    # TODO: Code here

    return finalResult