#Description

#Counts how many times a value appears using a loop.

Code
s = [1,2,2,3,3,4,4,2,2,5,5,1]
x = 2
count = 0

for num in s:
    if num == x:
        count += 1

print("Count:", count)

#Output
#Count: 4
