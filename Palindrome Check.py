# Description
# Checks whether a list is palindrome using two-pointer technique.

# Code
def palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return "Not Palindrome"
        i += 1
        j -= 1

    return "Palindrome"

s = [1,2,3,2,1]
print(palindrome(s))

# Output
# Palindrome
