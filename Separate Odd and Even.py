#Description
#Separates odd and even numbers into two lists.

#Code
s = [2,34,67,2,5,5]
odd = []
even = []

for num in s:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Odd :", odd)
print("Even:", even)

#Output
#Odd : [67, 5, 5]
#Even: [2, 34, 2]
