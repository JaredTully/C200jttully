#Write a lambda function that takes 3 strings and appends them
strApnd3 = lambda x,y,z : str(x) + str(y) + str(z)

print(strApnd3("first", "second", "third"))
print(strApnd3("test1", "test2", "test3"))

#Write a lambda function that takes 2 arguments and returns one raised the the power of the other and test it
firstPowerSecond = lambda x, y: x ** y

print(firstPowerSecond(3,3))
print(firstPowerSecond(2,4))


lst1 = [5, 2, 5, 7, 10]
lst2 = [10, 5, 1, 8, 15]
lst3 = ["deep", "in", "the", "hundred", "acre", "wood"]
#using lst1 and map, return a list that is the inverse (1/x) of each number of lst1

inverseLst1 = list(map(lambda x: 1/x, lst1))
print(inverseLst1)

#using lst1, lst2, and map, multiply lst1 by lst2 for each item
lstMultply = list(map(lambda x,y: x * y, lst1, lst2))
print(lstMultply)

#using lst3 and filter, return all words that have the letter r
LetR = [x for x in lst3 if ("r" in x) == True]
print(LetR)

#using list comprehension, return all words in lst3 that are 4 letters long, then add the letters "four" to the end.
plusFour = [x + "four" for x in lst3 if len(x) == 4]
print(plusFour)

#list comprehension inverse
lstComInver = [1/x for x in lst1]
print(lstComInver)

#list comprehenion list multiply
lstComMult = [x * y for x,y in zip(lst1,lst2)]
print(lstMultply)

#list comprehension letter r
lstComR = [x for x in lst3 if "r" in x]
print(lstComR)

#filter and map 4 letters add "four"
filterMap4 = map((lambda x: x if len(x) == 4), lst3)
print(filterMap4)