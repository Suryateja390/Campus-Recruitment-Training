#Description

#Changing nested elements affects both original and copied list in shallow copy.

#Code
s = [1, 2, [300, 300], [20, 30]]
s2 = s[:]

s[2][0] = 200

print("Original:", s)
print("Copy    :", s2)

#Output
#Original: [1, 2, [200, 300], [20, 30]]
#Copy    : [1, 2, [200, 300], [20, 30]]
