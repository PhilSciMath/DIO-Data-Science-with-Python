#!/bin/python

# Working with Sets


# Sets are iterable objects like lists, however they behave like sets in
# mathematics, it cannot contain duplicate elements. That means you can 
# give a list as argument to set() to automaticaly eliminate any duplicates.


# Creating a set:
languages = {'Python', 'Java', 'C', 'Python'}
print(languages)


# A list as argument:
fruits = set(["orange", "pear", "orange", "orange"])
print(fruits) # prints: {'orange', 'pear'}


# Notice that the printed result follows no particular order.
# Each time the program runs, the order of the elements change.
# An iterable (string) as argument:
print(set("avocado")) # prints: {'a', 'v', 'o', 'c', 'd'}


# A tuple as argument:
numbers = set((1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 1, 2))
print(numbers)


# Accessing values from a set. 
# A set doesn't support indexing as lists and tuples do. To get, say, 
# languages[1] we have to turn the set into a list first.
lang = list(languages)
print(lang[1])
# print(languages[1]) # uncomment and see the error!


# A for also works as expected:
for i in numbers:
    print(i, end=', ')
    

# The enumerate() method also works:
# But don't expect order, each time it runs the elements may change
# their position.
print("\n")
for i,j in enumerate(languages):
    print(f"{i} = {j}")
    

# Methos of the class set.
# We can do any of the mathematical set operations here.
print("\n")
X = {1, 2, 3, 'a'}
Y = {'a', 3, 'b', 4}
Z = {1}
print(f"X = {X}")
print(f"Y = {Y}")
print(f"Z = {Z}")
print(f"X union Y: {X.union(Y)}")
print(f"X intersection Y: {X.intersection(Y)}")
print(f"Y - X: {Y.difference(X)}")
print(f"X - Y: {X.difference(Y)}")
print(f"Y - X union X - Y: {Y.symmetric_difference(X)}") # all but the intesection
print(f"is Y subset of X: {Y.issubset(X)}")
print(f"is X subset of Y: {X.issubset(Y)}")
print(f"is Z subset of X: {Z.issubset(X)}")
print(f"is Y superset of X: {Y.issuperset(X)}") 
print(f"is X superset of Z: {X.issuperset(Z)}") 
print(f"are X and Z disjoint: {X.isdisjoint(Z)}") 
print(f"are Y and Z disjoint: {Y.isdisjoint(Z)}") 


# We can also add() and element to a set (if it is not there already):
Z.add(100)
print(f"put 100 into Z = {Z}")
Z.add(100)
print(f"put 100 into Z again = {Z}")


# .clear() makes the set empty:
Y.clear()
print(Y) # prints: set()


# .copy() generates a copy of the set
Y = X.copy()
print(Y)


# .discard() removes an element, if it exists, else ignore:
Z.discard(100)
print(Z)


# .pop() works, but it removes the first element instead of the last one:
print(f"\nX before pop: {X}")
X.pop()
print(f"X after pop: {X}")


# .remove(), works almost like .discard(), except that if the argumet is not
# in the set, it gives an error.
X.remove("a")
print(f'X after remove("a") = {X}')


# .len() works as with lists:
print(f"how many elements in X = {len(X)}")


# To check is an element is in the set, use 'in':
print(f"is 300 in X = {3000 in X}")
