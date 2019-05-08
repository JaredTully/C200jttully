def is_isogram(xword):
    diction = {}
    for i in range(len(xword)):
        if not xword[i] in diction.keys():
            diction[xword[i]] = 1
        else:
            return False
    return True 

words = ["dermatoglyphics","palindrome", "anagram"]

for w in words:
    print(is_isogram(w))