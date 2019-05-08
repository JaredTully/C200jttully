# Input Parameter: a list of numbers x
# Returns: the max number in list x (does not have to be unique)
def maxFor(x):
    i = x[0]
    for num in x:
        if num > i:
            i = num
    return i

# Input Parameter: a list of numbers x
# Returns: the minimal number value in list x (does not have to be unique)
def minFor(x):
    i = x[0]
    for num in x:
        if num < i:
            i = num
    return i

# Input Parameters: a number x and a list of numbers lst
# Returns: the list lst with all occurrences of x removed
def myRemove(x, lst):
    removeList = []
    for i in range(len(lst)):
        if x == lst[i]:
            removeList += [i]
    output = []
    for i in range(len(lst)):
        if not i in removeList:
            output += [lst[i]]
    return output
    

# Input Parameters: a number oldX, a number newX and a list of numbers lst
# Return Value: the list lst with all occurrences of oldX replaced with newX
def myReplace(oldX, newX, lst):
    changeList = []
    for i in range(len(lst)):
        if lst[i] == oldX:
            changeList += [i]
    output = []
    for i in range(len(lst)):
        if i in changeList:
            output += [newX]
        else:
            output += [lst[i]]
    return output


# Input Parameters: two lists x and y, x = [x1, x2, x3, ..., xk] and y = [y1, y2, y3, ..., yk]
# Returns: a new list with the following structure [x1, y1, x2, y2, x3, y3, ..., xk, yk]
# Note: assume that both lists are same length
def myLeftMerge(x, y):
    output = []
    for i in range(len(x)):
        output += [x[i]]
        output += [y[i]]
    return output


# Input Parameter: takes a list of lists of numbers [[x1, x2, x3, ...,  xn], [y1, y2, y3, ..., ym],...]
# Returns: a single list of numbers where each element is product of the inner list at that position, [x1*x2*x3*...*xn, y1*y2*y3*...*ym, ...]
def listProducts(x):
    output = []
    for lst in x:
        prod = lst[0]
        for i in range(1, len(lst)):
            prod = prod * lst[i]
        output += [prod]
    return output       
            

# Input Parameter: a list x of objects [x1, x2, x3,..., xn]
# Returns: a list with the string objects removed
def removeString(x):
    remove = []
    for i in range(len(x)):
        if type(x[i]) is str:
            #print("is str")
            remove += [i]
    output = []
    for i in range(len(x)):
        if not i in remove:
            output += [x[i]]
    return output


# Input Parameter: a string x
# Returns: the string with all vowels, upper and lower case removed
def removeVowels(x):
    vowels = ["a", "A", "e", "i", "I", "o", "O", "u", "U"]
    remove = []
    lst = list(x)
    for i in range(len(lst)):
        if x[i] in vowels:
            remove += [i]
    output = ""
    for i in range(len(lst)):
        if not i in remove:
            output = output + lst[i]
    return output


# Data
x = [1,42,24,22,61,100,0,42]
y = [2]
z = [555,333,222]
nlst = [x,y,z]
c = [0,1,1,0,2,1,4]
a = ["a","b","b", "a", "c","b","e"]
b = [1,1,2,1,1,2,1,1,2,1,3,1]


for i in nlst:
    print(minFor(i))
    print(maxFor(i))

print(myRemove("a",a))
print(myRemove("b",a))
print(myRemove("z",a))
print(myRemove(1,b))
print(myRemove(2,b))
print(myRemove("a",b))
print(myReplace("a",":)",a))
print(myReplace(1,0,b))
print(removeVowels("the lazy brown fox jumped over the eager dog"))
print(listProducts([[1],[2,3,4],[10,10,10,10]]))
print(removeString(["This",1, "is", "very", 3, [4], "exciting"]))
print(myLeftMerge(a,b))
print(myLeftMerge(['aa','bb'],[1,2]))
