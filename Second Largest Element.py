#Description

#Finds the second largest element in a list.

# Code
s = [1, 2, 3, 4, 3, 2, 4, 5]

first = second = float('-inf')

for num in s:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num

print("Second Largest:", second)

#Output
#Second Largest: 4
