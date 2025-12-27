
#Description

#Deep copy creates independent memory for nested elements.

# Code
import copy

s = [1, 2, [300, 400]]
s2 = copy.deepcopy(s)

s[2][0] = 500

print("Original:", s)
print("Copy    :", s2)

#Output
#Original: [1, 2, [500, 400]]
#Copy    : [1, 2, [300, 400]]
