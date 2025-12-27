#Description

#Finds the missing number from range 1..n.

Code
s = [1,3,4,5]
n = 5

missing = (n*(n+1))//2 - sum(s)
print("Missing:", missing)

#Output
#Missing: 2
