#Description
#This program demonstrates how shallow copy works in Python using list slicing.
#It shows that while the outer list is copied, the inner lists are still shared between the original list and the copied list.

# Demonstration of Shallow Copy in Python

# Original list with nested elements
s = [1, 2, [300, 300], [20, 30]]

# Creating a shallow copy
s2 = s[:]

# Displaying both lists
print("Original List:", s)
print("Copied List  :", s2)

#output:
#[1, 2, [300, 300], [20, 30]]
#[1, 2, [300, 300], [20, 30]]
