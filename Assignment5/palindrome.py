# Input Parameter: a string x
# Return Value: True if x is a palindrome, False otherwise
def palindrome(x):
    ret = True
    for i in range(0, len(x)):
        if x[i] != x[ (len(x)) - i -1 ]:
            ret = False
    return ret

print(palindrome("aba")) 
print(palindrome("a"))
print(palindrome("abba"))
print(palindrome("amanaplanacanalpanama")) 
print(palindrome("abca"))
print(palindrome("ac"))
print(palindrome("adabbba"))
print(palindrome("amandaplanacanalpanama"))