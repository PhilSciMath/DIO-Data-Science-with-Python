#!/bin/python

# Examples of Python lists

# A common explicit declaration of a list, all elements are strings
# Use '[]' and separate elements by comma
fruits = ["orange", "pineaple", "avocado"]
print(fruits)


# Empty list
empty = []
print(empty)


# Using the object 'list()', whichs takes an iterable, in this
# case the string "aeiou"
vowels = list("aeiou")
print(vowels)


# Lists may contain any object as element
stuff = ["car", 4.56, True]
print(stuff)


#Using the 'range()' object to generate an iterable for a list
foo = list(range(11))
print(foo)


# "any object" means any object even lists, then we call it
# nested lists
print("\n-------Nested Lists-------\n")
nested = ["nested", stuff, vowels, empty]
print(nested)


# Nested lists are matrices
matrix = [
    ["11 ", "12 ", "13"],
    ["21 ", "22 ", "23 "],
    ["31 ", "32 ", "33 "]
]
print(f"matrix = {matrix}")


# Getting the elements from a list
print(f"vowels[2] = {vowels[2]}")
print(f"stuff[1] = {stuff[1]}")


# The last element's index is -1
print(f"stuff[-1] = {stuff[-1]}")
print(f"vowels[-3] = {vowels[-3]}")


# Accessing element from a matrix
print("\n ---- Accessing Elements ----")
print(f"matrix[0][0] = {matrix[0][0]}")
print(f"matrix[2][2] = {matrix[2][2]}")
print(f"matrix[-1][2] = {matrix[-1][2]}")
print(f"matrix[2] = {matrix[2]}")


# Getting any range from a list by slicing it
print(f"vowels[1:4] = {vowels[1:4]}")
print(f"foo[0:11:2] = {foo[0:11:2]}")


# Inverse order
print(f"reverse vowels[::-1] = {vowels[::-1]} ")


# Using for to run through a list
for i in foo:
    print(f"{foo[i]} is even ") if i%2 == 0 else print(f"{foo[i]} is odd")
    

# Using 'enumerate()', it returns the index and the element
for index, element in enumerate(vowels):
    print(f"index = {index}; element = {element}")


# Filtering and comprehension of lists
# First let's try a normal filter to get evens, the 'append()' method puts more stuff in a list 
evens = []
for i in foo:
    if i%2 == 0:
        evens.append(i)
print(f"evens in foo: {evens}")


# The above method is slow, lets use list comprehension
evens2 = [i for i in foo if i%2 == 0]
print(evens2)


# Now suppose we want the odds to be squared
squared_odds = [i**2 for i in foo if not i%2 == 0]
print(squared_odds)


# Let's see some methods from the class 'list'

# .append() puts exactly ONE more element in a list, it may be a list
print("\n----- Methods from list -----\n")
print(f"fruits before append(): {fruits}")
fruits.append("mango")
print(f"fruits after append(): {fruits}")
fruits.append(vowels)
print(fruits)


# .clear() turns a lits empty
print(f"foo before clear(): {foo}")
foo.clear()
print(f"foo after clear(): {foo}")


# .copy() creates a different instance of an existing list
# it takes no argument, it just returns the list
foo = vowels.copy()
print(f"vowels = {vowels}")
print(f"foo    = {foo}")
print(f"vowels id = {id(vowels)}")
print(f"foo id = {id(foo)}")
foo.append("Skyrim")
print(f"foo with 1 more element = {foo}\n")


# .count() counts how many times an element appears in the list
fruits.append("orange")
print(f"fruits = {fruits}")
print(f"how many oranges = {fruits.count('orange')}")


# .extend() takes an iterable as argument and puts it into a list. 
# works as append(), but is able to put more elements each time
# it keeps same elements!
print(f"\nevens = {evens}")
evens.extend([i**2 for i in evens if i**2 > evens[-1]])
print(f"evens extended = {evens}")


# .index() retuns the index of the first occurrence of an element
print(f"\nindex of first orange = {fruits.index('orange')}")


# .pop() remove last element, or .pop(i) to remove ith-element
print(f"\nfruits before pop() = {fruits}")
print(f"fruits.pop() = {fruits.pop()}")
print(f"new fruits = {fruits}")
print(f"fruits.pop()  = {fruits.pop()}")
print(f"new fruits = {fruits}")
print(f"fruits.pop(0) = {fruits.pop(0)}")
print(f"new fruits = {fruits}\n")


# .remove(), it is like pop() but it takes the object as argument instead of its index
# it only removes the first occurrence of the element.
fruits.remove("avocado")
print(f"fruits.remove(avocado)  = {fruits}")


# .reverse() same as we did before with slice fruits[::-1]
print(f"\nevens           = {evens}")
evens.reverse()
print(f"evens.reverse() = {evens}")


# .sort(), it organizes a list
letters = ['a', 'o', 't', 'g', 'e', 'v', 'm']
print(f"\nletters                    = {letters}")
letters.sort()
print(f"letters.sort()             = {letters}")
letters.sort(reverse=True)
print(f"letters.sort(reverse=True) = {letters}")


# .sort(key=lamda x: len(x)), this one uses a lambda function to sort by the lenght
# of the element. So suppose we want fruits to be sorted like that:
fruits.extend(["avocado", "pear", "banana"])
print(f"fruits = {fruits}")
fruits.sort(key=lambda x: len(x))
print(f"fruits = {fruits}")
fruits.sort(key=lambda x: len(x), reverse=True)
print(f"fruits = {fruits}")


# Some built in methods:
# len() is a method that takes the size of iterables
print(f"how many fruits: {len(fruits)}")


# sorted(), works like .sort(), but is built in")
print(sorted(fruits, key=lambda x: len(x), reverse=True))
