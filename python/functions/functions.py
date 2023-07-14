#!/bin/python

# Dealing with functions


# How to declare a function in Python
def hello():
    print("Hello World!")

def message(name):
    print(f"Wellcome {name}")

def new_message(name = "#####"):
    print(f"Wellcome {name}!")

hello()
message(name="Batman")
new_message()
new_message(name="Superman")


# Returning values
def addition(numbers):
    return sum(numbers)
print(sum([10, 20, 5]))


# Returning multiple values
def multiply_and_divide(x, y):
    mult = x * y
    div1 = x / y
    div2 = y / x
    return mult, div1, div2
result = multiply_and_divide(10, 100)
print(result)


