#Description
#Merges two sorted arrays into one sorted array.

#Code
a = [1,2,5,8,23]
b = [3,4,7,32,34]

i = j = 0
res = []

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1

res.extend(a[i:])
res.extend(b[j:])

print("Merged:", res)

#Output
#Merged: [1, 2, 3, 4, 5, 7, 8, 23, 32, 34]
