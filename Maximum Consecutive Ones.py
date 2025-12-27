#Description

#Finds the longest sequence of continuous 1s.

#Code
s = [1,0,1,1,0,0,1,1,1,1]
count = 0
result = 0

for num in s:
    if num == 1:
        count += 1
        result = max(result, count)
    else:
        count = 0
print("Max Consecutive 1s:", result)

#Output
#Max Consecutive 1s: 4
