#Description

#Rotates the array by k positions to the right.

Code
s = [1,2,3,4,5]
k = 1

rotated = s[-k:] + s[:-k]
print("Rotated:", rotated)

#Output
#Rotated: [5, 1, 2, 3, 4]
