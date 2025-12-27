"""
File Name   : hashing_demo.py
Author      : Surys Teja
Description : This program demonstrates how Python uses hashing
              and how elements are mapped into a limited number
              of positions using modulo operation.
"""

# Creating a set of integers
s = {1, 4, 10, 25, 67}

print("Original Set:", s)
print("Set Size:", len(s))
print("-" * 40)

for num in s:
    # Compute hash value of the number
    hash_value = hash(num)
    
    index_position = hash_value % len(s)
    print(f"Number: {num}")
    print(f"Hash Value: {hash_value}")
    print(f"Mapped Index (hash % {len(s)}): {index_position}")
    print("-" * 40)

Set: {1, 4, 10, 25, 67}
Size: 5

Number: 1
Hash: 1
Index: 1

Number: 4
Hash: 4
Index: 4

Number: 10
Hash: 10
Index: 0

Number: 25
Hash: 25
Index: 0

Number: 67
Hash: 67
Index: 2
