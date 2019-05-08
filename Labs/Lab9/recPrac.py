def myRemove(x, cont):
    """
    Recursively remove every occurence of `x` in `cont` and return a list 
    that has all the contents of `cont` that are not `x`
    
    You cannot use the list operation .remove in this function
    """
    if cont:
        if cont[0] != x:
            return [cont[0]] + myRemove(x, cont[1:])
        else:
            return myRemove(x, cont[1:])
    else:
        return []

def myReplace(old, new, cont):
    """
    Recursively return a list of all contents of `cont` but any value that is 
    `old` is replaced with `new`
    """
    if cont:
        if cont[0] == old:
            return [new] + myReplace(old, new, cont[1:])
        else:
            return [cont[0]] + myReplace(old, new, cont[1:])
    else:
        return []

def palindrome(string):
    """ 
    Recursively returns true if the string is a palindrome. 
    
    You CANNOT use a list iterator i.e. string[::-1]
    """
    strLng = length(string)
     

def removeString(cont):
    """
    Recursively returns the contents of list `cont`, not including any that are strings. 
    """
    pass

def length(cont):
    """
    Recursively returns the length of the cont.
    
    You can not use the `len()` built-in function here
    """
    if cont:
        return 1 + length(cont[1:])
    else:
        return 0

def removePos(x, cont):
    """
    Recursively removes an item from the list `cont` that is at `x`.
    Returns a list of all items from `cont` that are not were not at the `x` position
    Example: removePos(1, ['a', 'b', 'c']) --> ['a', 'c']
    """
    pass

def sum2Dlist(mat):
    """
    Recursively go through and sum all the values from each row and add the result of
    each row together to get a final value
    ex) 
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]] ---> 45
    Returns an integer
    """
    pass