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
