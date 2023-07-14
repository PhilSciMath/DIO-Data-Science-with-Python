#!/bin/python

# This file has examples of working with tuples in Python
# The main difference between tuples and lists is that the tuples are immutable.
# Once a tuple is created, it will keep its values till the end of the program.
# Use tuples when you need values that cannot change. It helps to see lists
# as variable sequences while tuples as constant sequences.


# Examples on how to create tuples:
fruits = ("orange", "mango", "pear", ) # comma at the end is good practice
countries = ("Brasil", )

rpg = tuple("Skyrim") # here the comma is not needed, each letter becomes an element
numbers = tuple([34, 12, 567]) # values in the list become a tuple

print(fruits)
print(countries)
print(rpg)
print(numbers)


# Accessing the tuple's values is the same as we do for lists, even slicing.
print(fruits[1])
print(rpg[4])
print(rpg[1:5])
print(rpg[::-1])


# Tuples can also be nested
matrix = (
    ("a", 45, "y"),
    (.7, 2, 10000),
    ("z", "zz", "zzz"),
)
print(matrix)
print(matrix[-1][-1])


# Other operations work as for lists
for index,value in enumerate(fruits):
    print(f"{index} = {value}")
    
    
# A tuple has fewer methos, since it can't remove or add elements.
print(f"number of oranges = {fruits.count('orange')}")
print(f"index of orange = {fruits.index('orange')}")
print(f"how many fruits = {len(fruits)}")

    
    
    
    
    
    