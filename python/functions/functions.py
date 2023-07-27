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
# It returns the values as a tuple
def multiply_and_divide(x, y):
    mult = x * y
    div1 = x / y
    div2 = y / x
    return mult, div1, div2
result = multiply_and_divide(10, 100)
print(result)



# Arguments and return values may also be dictionaries
def save_car_in_database(brand, year, color):
    # do stuff
    print(f"Car successfuly saved: {brand}, {year}, {color}")
# and these are possible ways of doing it:
save_car_in_database("Ford", 1980, "black")
# or
save_car_in_database(brand="Mazda", year=1990, color="red")
# or (notice the two stars)
save_car_in_database(**{"brand": "Honda", "year": 2000, "color": "green"})
# *args: the argument goes in as a tuple
# **kwargs: arguments are dictionaries, as above.



# More examples with *args and **kwargs
def show_text(date, *args, **kwargs):
    text = "\n".join(args)
    meta_data = " ".join([f"{key.title()}: {value}" for key, value in kwargs.items()])
    message = f"\n{date}\n\n{text}\n\n{meta_data}"
    print(message)

show_text(
    "Jul, 14, 2023",
    "Zen of Python",     
    "Beautiful is better than ugly.", 
    "Explicit is better than implicit",
    autor="Tim Peters", 
    year=1999
    )
# Note: the names *args and **kwargs could by any thing, like:
# *stuff_in_list_format and **amazing_dictionary would both be valid.



# Arguments by position and keyword
# We can force how argument are passed to the function. Everything till "/",
# must be by position. Between "/" and "*" may be both, and after "*" only
# key=value pairs are valid.
# def f(pos1, pos2, /, foo, key0="val0", *, key1="val1", key2="val2")
print("\n\n")
def create_car(brand, year, plate, /, engine, fuel_type):
    print(brand, year, plate, engine, fuel_type)

create_car("Honda", 1978, "HND-1234", engine="2.0", fuel_type="gas")
# The following should give an error
# create_car(brand="Honda", 1978, "HND-1234", engine="2.0", fuel_type="gas")
# So the following forces the argument to be named, because the "*":
# def create_car(*, brand, year, plate, engine, fuel_type)



# Functions are first class objects, we can attribute them to variables, pass
# them as arguments to other functions, use them as values in data structures.
# Here's an example of a function as argument:
def addition(a, b):
    return a + b

def subtract(a, b):
    return a - b

def print_result(a, b, some_function):
    result = some_function(a, b)
    print(f"Result is {result}\n")

print_result(10, 10, addition)
print_result(10, 10, subtract)

# Attributing a function to a variable:
num = addition      # no "()"
print(num(4, 6))



# Global and Local scope.
# What is made inside the block of a function is local to it. Variables defined
# outside the block are global, and to specify you want to use it inside the
# function, use the "global" reserved word, which is not good practice.
income = 1000

def add_to_income(bonus):
    global income
    income += bonus
    return income

add_to_income(500)
print(income)











