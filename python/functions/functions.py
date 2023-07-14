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